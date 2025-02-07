from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadFileView.as_view(), name='upload_file'),
    path('tutorial/', views.TutorialView.as_view(template_name='analytics/tutorial.html'), name='tutorial'),
]