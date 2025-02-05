from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadedFile
import json

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            following_file = request.FILES['following_file']
            followers_file = request.FILES['followers_file']

            UploadedFile.objects.create(file=following_file)
            UploadedFile.objects.create(file=followers_file)

            return show_results(request, following_file, followers_file)
    else:
        form = UploadFileForm()
    return render(request, 'analytics/upload.html', {'form': form})

def show_results(request, following_file, followers_file):
    following_data = json.load(following_file)
    followers_data = json.load(followers_file)
    
    following_set = set(following_data['users'])
    followers_set = set(followers_data['users'])
    
    context = {
        'following_count': len(following_set),
        'followers_count': len(followers_set),
        'mutual_follow': len(following_set & followers_set),
        'non_follow_back': list(following_set - followers_set),
        'not_following_back': list(followers_set - following_set),
    }
    return render(request, 'analytics/results.html', context)