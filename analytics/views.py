from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
import json
import os
from django.conf import settings

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            following_file = request.FILES['following_file']
            followers_file = request.FILES['followers_file']

            following_instance = UploadedFile.objects.create(file=following_file)
            followers_instance = UploadedFile.objects.create(file=followers_file)

            return redirect('show_results', following_id=following_instance.id, followers_id=followers_instance.id)
    else:
        form = UploadFileForm()
    return render(request, 'analytics/upload.html', {'form': form})

def show_results(request, following_id, followers_id):
    following_instance = UploadedFile.objects.get(id=following_id)
    followers_instance = UploadedFile.objects.get(id=followers_id)
    
    following_file_path = os.path.join(settings.MEDIA_ROOT, following_instance.file.name)
    followers_file_path = os.path.join(settings.MEDIA_ROOT, followers_instance.file.name)
    
    with open(following_file_path, 'r') as following_file:
        following_data = json.load(following_file)
    
    with open(followers_file_path, 'r') as followers_file:
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