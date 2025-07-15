"""
Utility functions for internationalization and content management
"""

from django.utils import translation
from .data.HomeData import HOME_DATA
from .data.UploadData import UPLOAD_DATA
from .data.ZipUploadData import ZIP_UPLOAD_DATA
from .data.TextInputData import TEXT_INPUT_DATA
from .data.TutorialData import TUTORIAL_DATA
from .data.ResultsData import RESULTS_DATA
from .data.BaseData import BASE_DATA

def get_current_language():
    """Get the current active language code"""
    language = translation.get_language()
    # Map Django language codes to our data keys
    if language and language.startswith('id'):
        return 'id'
    elif language and language.startswith('zh'):
        return 'zh'
    elif language and language.startswith('es'):
        return 'es'
    elif language and language.startswith('ja'):
        return 'ja'
    elif language and language.startswith('pt'):
        return 'pt'
    elif language and language.startswith('fr'):
        return 'fr'
    return 'en'

def get_content_data(data_dict, language=None):
    """
    Get content data for the specified language
    Falls back to English if language not found
    """
    if language is None:
        language = get_current_language()
    
    return data_dict.get(language, data_dict.get('en', {}))

def get_home_data(language=None):
    """Get home page content for specified language"""
    return get_content_data(HOME_DATA, language)

def get_upload_data(language=None):
    """Get upload page content for specified language"""
    return get_content_data(UPLOAD_DATA, language)

def get_zip_upload_data(language=None):
    """Get ZIP upload page content for specified language"""
    return get_content_data(ZIP_UPLOAD_DATA, language)

def get_text_input_data(language=None):
    """Get text input page content for specified language"""
    return get_content_data(TEXT_INPUT_DATA, language)

def get_tutorial_data(language=None):
    """Get tutorial page content for specified language"""
    return get_content_data(TUTORIAL_DATA, language)

def get_results_data(language=None):
    """Get results page content for specified language"""
    return get_content_data(RESULTS_DATA, language)

def get_base_data(language=None):
    """Get base template content for specified language"""
    return get_content_data(BASE_DATA, language)

def inject_i18n_context(request):
    """
    Context processor to inject internationalization data into templates
    This can be used as a context processor in settings
    """
    current_lang = get_current_language()
    base_data = get_base_data(current_lang)
    
    return {
        'current_language': current_lang,
        'is_indonesian': current_lang == 'id',
        'is_english': current_lang == 'en',
        'is_chinese': current_lang == 'zh',
        'is_spanish': current_lang == 'es',
        'is_japanese': current_lang == 'ja',
        'is_portuguese': current_lang == 'pt',
        'is_french': current_lang == 'fr',
        **base_data  # Spread base template data into context
    }
