from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('upload/', views.UploadFileView.as_view(), name='upload_file'),
    path('zip/', views.ZipUploadView.as_view(), name='zip_upload'),
    path('text/', views.TextInputView.as_view(), name='text_input'),
    path('tutorial/', views.TutorialView.as_view(), name='tutorial'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('.well-known/security.txt', views.security_txt, name='security_txt'),
    path('set-language/', views.LanguageSwitchView.as_view(), name='set_language'),
    path('language-info/', views.LanguageInfoView.as_view(), name='language_info'),
]