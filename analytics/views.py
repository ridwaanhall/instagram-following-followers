import json
import logging
import os
import zipfile

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .analysis import analyze
from .forms import UploadFileForm, ZipUploadForm
from .utils import (
    detect_language_from_request, get_analyzer_data, get_home_data, get_language_info, get_privacy_data,
    get_results_data, get_terms_data, get_text_input_data, get_tutorial_data, get_upload_data,
    get_zip_upload_data, is_supported_language,
)

logger = logging.getLogger(__name__)


def safe_next_url(request, candidate):
    """Only follow ``next``/Referer when it points back at this site."""
    if candidate and url_has_allowed_host_and_scheme(
        candidate, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return candidate
    return "/"


class LanguageSwitchView(View):
    """Switch the interface language via POST (form) or GET (``?lang=``)."""

    def _activate(self, request, language_code):
        request.session[settings.LANGUAGE_SESSION_KEY] = language_code
        translation.activate(language_code)
        request.LANGUAGE_CODE = language_code

    def post(self, request, *args, **kwargs):
        language_code = request.POST.get('language')
        wants_json = request.headers.get('Content-Type') == 'application/json'

        if language_code and is_supported_language(language_code):
            self._activate(request, language_code)
            if wants_json:
                return JsonResponse({
                    'status': 'success',
                    'language': language_code,
                    'language_name': dict(settings.LANGUAGES).get(language_code, language_code),
                })
        elif wants_json:
            return JsonResponse({'status': 'error', 'message': 'Unsupported language code'}, status=400)

        return redirect(safe_next_url(request, request.POST.get('next') or request.META.get('HTTP_REFERER')))

    def get(self, request, *args, **kwargs):
        language_code = request.GET.get('lang')
        if language_code and is_supported_language(language_code):
            self._activate(request, language_code)
        return redirect(safe_next_url(request, request.GET.get('next') or request.META.get('HTTP_REFERER')))


class LanguageInfoView(View):
    """Current language information as JSON."""

    def get(self, request, *args, **kwargs):
        lang_info = get_language_info()
        return JsonResponse({
            'current_language': lang_info['current'],
            'current_language_name': lang_info['current_name'],
            'available_languages': lang_info['available'],
            'detected_language': detect_language_from_request(request),
            'browser_languages': request.META.get('HTTP_ACCEPT_LANGUAGE', ''),
            'supported_codes': lang_info['supported_codes'],
        })


class ContentView(TemplateView):
    """TemplateView whose context comes from one of the ``analytics/data`` getters."""
    content = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.content())
        return context


class HomeView(ContentView):
    template_name = 'analytics/home.html'
    content = staticmethod(lambda: {**get_home_data(), **get_analyzer_data(), 'rs': get_results_data()})


class TutorialView(ContentView):
    template_name = 'analytics/tutorial.html'
    content = staticmethod(get_tutorial_data)


class PrivacyView(ContentView):
    """Privacy notice. English only - see analytics/data/PrivacyData.py."""
    template_name = 'analytics/legal.html'
    content = staticmethod(get_privacy_data)


class TermsView(ContentView):
    """Terms of use. English only - see analytics/data/TermsData.py."""
    template_name = 'analytics/legal.html'
    content = staticmethod(get_terms_data)


SECURITY_TXT = """Contact: mailto:founder@rone.dev
Expires: 2027-09-27T00:00:00.000Z
Preferred-Languages: en, id
Policy: https://rone.dev/security
Canonical: https://igstats.rone.dev/.well-known/security.txt
"""


def security_txt(request):
    """RFC 9116 security contact."""
    return HttpResponse(SECURITY_TXT, content_type='text/plain; charset=utf-8')


class BaseAnalyticsView(FormView):
    """Shared by the three input methods; each subclass only reads its input."""
    success_url = reverse_lazy('home')
    content = None
    method = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.content())
        context.update(get_analyzer_data())
        context['method'] = self.method
        return context

    def read_input(self, form):
        """Return ``(following_data, followers_data)`` or raise ``ValueError``."""
        raise NotImplementedError

    def form_valid(self, form):
        try:
            following_data, followers_data = self.read_input(form)
            context = analyze(following_data, followers_data)
        except ValueError as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)
        except Exception as e:
            logger.error("Unexpected error while analyzing %s input: %s", self.method, e)
            messages.error(self.request, "An error occurred while analyzing the data. Please check your inputs.")
            return self.form_invalid(form)

        context.update(get_results_data())
        return render(self.request, 'analytics/results.html', context)


class UploadFileView(BaseAnalyticsView):
    template_name = 'analytics/upload.html'
    form_class = UploadFileForm
    content = staticmethod(get_upload_data)
    method = 'files'

    def read_input(self, form):
        following_file = self.request.FILES.get('following_file')
        followers_file = self.request.FILES.get('followers_file')
        if not following_file or not followers_file:
            raise ValueError("Please upload both following and followers files.")
        try:
            return json.load(following_file), json.load(followers_file)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file format. Please check your files and try again.")


class TextInputView(BaseAnalyticsView):
    template_name = 'analytics/text_input.html'
    form_class = UploadFileForm
    content = staticmethod(get_text_input_data)
    method = 'text'

    def read_input(self, form):
        following_text = form.cleaned_data.get('following_text')
        followers_text = form.cleaned_data.get('followers_text')
        if not following_text or not followers_text:
            raise ValueError("Please provide both following and followers JSON data.")
        try:
            return json.loads(following_text), json.loads(followers_text)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input format. Please check and try again.")


class ZipUploadView(BaseAnalyticsView):
    template_name = 'analytics/zip_upload.html'
    form_class = ZipUploadForm
    content = staticmethod(get_zip_upload_data)
    method = 'zip'
    wanted = {'following.json': 'following', 'followers_1.json': 'followers'}

    def read_input(self, form):
        zip_file = self.request.FILES.get('zip_file')
        if not zip_file:
            raise ValueError("Please upload a ZIP file.")
        try:
            with zipfile.ZipFile(zip_file) as archive:
                names = archive.namelist()
                found = {}
                for path in names:
                    key = self.wanted.get(os.path.basename(path).lower())
                    if key:
                        found[key] = path
                missing = [name for name, key in self.wanted.items() if key not in found]
                if missing:
                    available = ', '.join(os.path.basename(n) for n in names if n.endswith('.json'))
                    raise ValueError(
                        f"Could not find required files: {', '.join(missing)}. "
                        f"Available JSON files: {available or 'none'}"
                    )
                with archive.open(found['following']) as f:
                    following_data = json.load(f)
                with archive.open(found['followers']) as f:
                    followers_data = json.load(f)
        except zipfile.BadZipFile:
            raise ValueError("Invalid ZIP file format.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in one of the files: {e}")
        return following_data, followers_data
