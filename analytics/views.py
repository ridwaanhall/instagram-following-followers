from django.shortcuts import render, redirect
from .forms import UploadFileForm
import json

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            following_file = request.FILES.get('following_file')
            followers_file = request.FILES.get('followers_file')
            following_text = form.cleaned_data.get('following_text')
            followers_text = form.cleaned_data.get('followers_text')

            if following_file and followers_file:
                return show_results_from_files(request, following_file, followers_file)
            elif following_text and followers_text:
                return show_results_from_text(request, following_text, followers_text)
    else:
        form = UploadFileForm()
    return render(request, 'analytics/upload.html', {'form': form})

def show_results_from_files(request, following_file, followers_file):
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
        'following_count': len(following_set),
        'followers_count': len(followers_set),
        'mutual_follow': len(following_set & followers_set),
        'non_follow_back': list(following_set - followers_set),
        'not_following_back': list(followers_set - following_set),
    }
    return render(request, 'analytics/results.html', context)

def show_results_from_text(request, following_text, followers_text):
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
        'following_count': len(following_set),
        'followers_count': len(followers_set),
        'mutual_follow': len(following_set & followers_set),
        'non_follow_back': list(following_set - followers_set),
        'not_following_back': list(followers_set - following_set),
    }
    return render(request, 'analytics/results.html', context)