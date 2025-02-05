from django import forms

class UploadFileForm(forms.Form):
    following_file = forms.FileField()
    followers_file = forms.FileField()