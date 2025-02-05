from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('results/files/', views.show_results_from_files, name='show_results_from_files'),
    path('results/text/', views.show_results_from_text, name='show_results_from_text'),
]