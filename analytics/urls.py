from django.urls import path
from .views import UploadFileView

urlpatterns = [
    path('', UploadFileView.as_view(), name='upload_file'),
]