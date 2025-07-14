from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('upload/', views.UploadFileView.as_view(), name='upload_file'),
    path('zip/', views.ZipUploadView.as_view(), name='zip_upload'),
    path('text/', views.TextInputView.as_view(), name='text_input'),
    path('tutorial/', views.TutorialView.as_view(template_name='analytics/tutorial.html'), name='tutorial'),
]