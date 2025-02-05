from django import forms
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    if not value.name.endswith('.json') and not value.name.endswith('.txt'):
        raise ValidationError('Only .json and .txt files are allowed.')

class UploadFileForm(forms.Form):
    following_file = forms.FileField(required=False, validators=[validate_file_extension])
    followers_file = forms.FileField(required=False, validators=[validate_file_extension])
    following_text = forms.CharField(widget=forms.Textarea, required=False)
    followers_text = forms.CharField(widget=forms.Textarea, required=False)