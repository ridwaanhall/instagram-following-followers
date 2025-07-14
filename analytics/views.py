from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import UploadFileForm
import json
import logging
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = 'analytics/home.html'

class BaseAnalyticsView(FormView):
    success_url = reverse_lazy('home')

    def process_data(self, following_data, followers_data):
        try:
            following_set = {
                user['value']
                for item in following_data.get('relationships_following', [])
                for user in item.get('string_list_data', [])
            }

            followers_set = {
                user['value']
                for item in followers_data
                for user in item.get('string_list_data', [])
            }

            context = {
                'count_following_count': len(following_set),
                'count_followers_count': len(followers_set),
                'count_mutual_follow': len(following_set & followers_set),
                'count_non_follow_back': len(following_set - followers_set),
                'count_not_following_back': len(followers_set - following_set),
                'list_mutual_follow': list(following_set & followers_set),
                'list_non_follow_back': list(following_set - followers_set),
                'list_not_following_back': list(followers_set - following_set),
            }
            return render(self.request, 'analytics/results.html', context)

        except Exception as e:
            logger.error(f"Unexpected error while processing data: {e}")
            messages.error(self.request, "An error occurred while analyzing the data. Please check your inputs.")
            return self.form_invalid(self.form_class())

class UploadFileView(BaseAnalyticsView):
    template_name = 'analytics/upload.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        try:
            following_file = self.request.FILES.get('following_file')
            followers_file = self.request.FILES.get('followers_file')

            if not following_file or not followers_file:
                messages.error(self.request, "Please upload both following and followers files.")
                return self.form_invalid(form)

            # Ensure file type validation
            if not following_file.name.endswith('.json') or not followers_file.name.endswith('.json'):
                messages.error(self.request, "Uploaded files must be in JSON format.")
                return self.form_invalid(form)

            following_data = json.load(following_file)
            followers_data = json.load(followers_file)

            return self.process_data(following_data, followers_data)
        
        except json.JSONDecodeError:
            messages.error(self.request, "Invalid JSON file format. Please check your files and try again.")
            return self.form_invalid(form)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            messages.error(self.request, "An unexpected error occurred. Please try again later.")
            return self.form_invalid(form)

class TextInputView(BaseAnalyticsView):
    template_name = 'analytics/text_input.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        try:
            following_text = form.cleaned_data.get('following_text')
            followers_text = form.cleaned_data.get('followers_text')

            if not following_text or not followers_text:
                messages.error(self.request, "Please provide both following and followers JSON data.")
                return self.form_invalid(form)

            following_data = json.loads(following_text)
            followers_data = json.loads(followers_text)

            return self.process_data(following_data, followers_data)
        
        except json.JSONDecodeError:
            messages.error(self.request, "Invalid JSON input format. Please check and try again.")
            return self.form_invalid(form)
        except Exception as e:
            logger.error(f"Unexpected error while processing text input: {e}")
            messages.error(self.request, "An unexpected error occurred while processing the input.")
            return self.form_invalid(form)
    
class TutorialView(TemplateView):
    template_name = 'analytics/tutorial.html'