"""
Automatic language selection: session preference, then ``?lang=``, then the
browser's ``Accept-Language`` header, then the default.
"""

from django.conf import settings
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin

from .utils import detect_language_from_browser_header, is_supported_language

SKIP_PREFIXES = ('/admin/', '/static/', '/media/', '/api/', '/favicon.ico', '/robots.txt', '/sitemap.xml')


class AutoLanguageDetectionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info.startswith(SKIP_PREFIXES):
            return None

        session_key = settings.LANGUAGE_SESSION_KEY
        session_language = request.session.get(session_key)
        if session_language and is_supported_language(session_language):
            language = session_language
        else:
            lang_param = request.GET.get('lang') or request.POST.get('lang')
            if lang_param and is_supported_language(lang_param):
                language = lang_param
            else:
                language = detect_language_from_browser_header(request) or settings.LANGUAGE_CODE
            request.session[session_key] = language

        translation.activate(language)
        request.LANGUAGE_CODE = language
        return None
