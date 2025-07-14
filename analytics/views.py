from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import UploadFileForm, ZipUploadForm
import json
import logging
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
import zipfile
import tempfile
import os

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

class ZipUploadView(BaseAnalyticsView):
    template_name = 'analytics/zip_upload.html'
    form_class = ZipUploadForm

    def find_json_files_in_zip(self, zip_file):
        """
        Find followers_1.json and following.json files in the ZIP archive.
        These files can be in any subdirectory, commonly in followers_and_following folder.
        """
        following_data = None
        followers_data = None
        
        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                # List all files in the ZIP
                file_list = zip_ref.namelist()
                
                # Search for the required JSON files
                following_file_path = None
                followers_file_path = None
                
                for file_path in file_list:
                    file_name = os.path.basename(file_path).lower()
                    
                    # Look for following.json
                    if file_name == 'following.json':
                        following_file_path = file_path
                    
                    # Look for followers_1.json
                    elif file_name == 'followers_1.json':
                        followers_file_path = file_path
                
                # Extract and read the files if found
                if following_file_path:
                    with zip_ref.open(following_file_path) as f:
                        following_data = json.load(f)
                        logger.info(f"Found following.json at: {following_file_path}")
                
                if followers_file_path:
                    with zip_ref.open(followers_file_path) as f:
                        followers_data = json.load(f)
                        logger.info(f"Found followers_1.json at: {followers_file_path}")
                
                if not following_data or not followers_data:
                    missing_files = []
                    if not following_data:
                        missing_files.append("following.json")
                    if not followers_data:
                        missing_files.append("followers_1.json")
                    
                    logger.warning(f"Missing files in ZIP: {missing_files}")
                    logger.info(f"Available files in ZIP: {[os.path.basename(f) for f in file_list if f.endswith('.json')]}")
                    
                    return None, None, f"Could not find required files: {', '.join(missing_files)}. Available JSON files: {', '.join([os.path.basename(f) for f in file_list if f.endswith('.json')])}"
                
                return following_data, followers_data, None
                
        except zipfile.BadZipFile:
            return None, None, "Invalid ZIP file format."
        except json.JSONDecodeError as e:
            return None, None, f"Invalid JSON format in one of the files: {str(e)}"
        except Exception as e:
            logger.error(f"Error processing ZIP file: {e}")
            return None, None, f"Error processing ZIP file: {str(e)}"

    def form_valid(self, form):
        try:
            zip_file = self.request.FILES.get('zip_file')
            
            if not zip_file:
                messages.error(self.request, "Please upload a ZIP file.")
                return self.form_invalid(form)

            # Process the ZIP file
            following_data, followers_data, error_message = self.find_json_files_in_zip(zip_file)
            
            if error_message:
                messages.error(self.request, error_message)
                return self.form_invalid(form)
            
            # Process the extracted data using the parent class method
            return self.process_data(following_data, followers_data)
            
        except Exception as e:
            logger.error(f"Unexpected error in ZIP upload: {e}")
            messages.error(self.request, "An unexpected error occurred while processing the ZIP file.")
            return self.form_invalid(form)