from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('results/<int:following_id>/<int:followers_id>/', views.show_results, name='show_results'),
]