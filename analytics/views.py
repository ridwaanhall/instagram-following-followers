from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UploadFileForm
import json
from django.views.generic.base import TemplateView

class UploadFileView(FormView):
    template_name = 'analytics/upload.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        following_file = self.request.FILES.get('following_file')
        followers_file = self.request.FILES.get('followers_file')
        following_text = form.cleaned_data.get('following_text')
        followers_text = form.cleaned_data.get('followers_text')

        if following_file and followers_file:
            return self.show_results_from_files(following_file, followers_file)
        elif following_text and followers_text:
            return self.show_results_from_text(following_text, followers_text)
        return super().form_valid(form)

    def show_results_from_files(self, following_file, followers_file):
        following_data = json.load(following_file)
        followers_data = json.load(followers_file)
        
        following_set = set()
        for item in following_data['relationships_following']:
            for user in item['string_list_data']:
                following_set.add(user['value'])
        
        followers_set = set()
        for item in followers_data:
            for user in item['string_list_data']:
                followers_set.add(user['value'])
        
        context = {
            'count_following_count': len(following_set),
            'count_followers_count': len(followers_set),
            'count_mutual_follow': len(following_set & followers_set),
            'count_non_follow_back': len(following_set - followers_set),
            'count_not_following_back': len(followers_set - following_set),
            'list_non_follow_back': list(following_set - followers_set),
            'list_not_following_back': list(followers_set - following_set),
        }
        return render(self.request, 'analytics/results.html', context)

    def show_results_from_text(self, following_text, followers_text):
        following_data = json.loads(following_text)
        followers_data = json.loads(followers_text)
        
        following_set = set()
        for item in following_data['relationships_following']:
            for user in item['string_list_data']:
                following_set.add(user['value'])
        
        followers_set = set()
        for item in followers_data:
            for user in item['string_list_data']:
                followers_set.add(user['value'])
        
        context = {
            'count_following_count': len(following_set),
            'count_followers_count': len(followers_set),
            'count_mutual_follow': len(following_set & followers_set),
            'count_non_follow_back': len(following_set - followers_set),
            'count_not_following_back': len(followers_set - following_set),
            'list_non_follow_back': list(following_set - followers_set),
            'list_not_following_back': list(followers_set - following_set),
        }
        return render(self.request, 'analytics/results.html', context)
    
class TutorialView(TemplateView):
    template_name = 'analytics/tutorial.html'
