"""
Utility functions for internationalization and content management
"""

from django.utils import translation
from django.conf import settings
from .data.HomeData import HOME_DATA
from .data.UploadData import UPLOAD_DATA
from .data.ZipUploadData import ZIP_UPLOAD_DATA
from .data.TextInputData import TEXT_INPUT_DATA
from .data.TutorialData import TUTORIAL_DATA
from .data.ResultsData import RESULTS_DATA
from .data.BaseData import BASE_DATA

def is_supported_language(language_code):
    """
    Check if a language code is supported by the application
    """
    supported_codes = [code for code, name in settings.LANGUAGES]
    return language_code in supported_codes


def get_language_info():
    """
    Get comprehensive language information including current language and available options
    """
    current_lang = get_current_language()
    
    return {
        'current': current_lang,
        'current_name': dict(settings.LANGUAGES).get(current_lang, current_lang),
        'available': dict(settings.LANGUAGES),
        'supported_codes': [code for code, name in settings.LANGUAGES],
    }


def get_client_ip(request):
    """
    Get the client's IP address from request headers
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def detect_language_from_request(request):
    """
    Comprehensive language detection from request
    Priority: URL parameter > Session > Browser Accept-Language > Geolocation > Default
    """
    # 1. Check for explicit language parameter in URL
    lang_param = request.GET.get('lang') or request.POST.get('lang')
    if lang_param and is_supported_language(lang_param):
        return lang_param
    
    # 2. Check session for stored language preference
    session_lang = request.session.get(settings.LANGUAGE_SESSION_KEY)
    if session_lang and is_supported_language(session_lang):
        return session_lang
    
    # 3. Parse browser Accept-Language header
    browser_lang = detect_language_from_browser_header(request)
    if browser_lang:
        return browser_lang
    
    # 4. Fallback to default language
    return settings.LANGUAGE_CODE


def detect_language_from_browser_header(request):
    """
    Detect language from browser Accept-Language header
    """
    accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    if not accept_language:
        return None
    
    # Language mapping for better browser compatibility
    language_map = {
        'en': 'en', 'en-us': 'en', 'en-gb': 'en', 'en-au': 'en', 'en-ca': 'en',
        'id': 'id', 'id-id': 'id',
        'zh': 'zh-hans', 'zh-cn': 'zh-hans', 'zh-hans': 'zh-hans', 'zh-sg': 'zh-hans',
        'es': 'es', 'es-es': 'es', 'es-mx': 'es', 'es-ar': 'es', 'es-co': 'es',
        'ja': 'ja', 'ja-jp': 'ja',
        'pt': 'pt-br', 'pt-br': 'pt-br', 'pt-pt': 'pt-br',
        'fr': 'fr', 'fr-fr': 'fr', 'fr-ca': 'fr', 'fr-be': 'fr',
        'de': 'de', 'de-de': 'de', 'de-at': 'de', 'de-ch': 'de',
    }
    
    # Parse and sort languages by quality
    languages = []
    for item in accept_language.split(','):
        item = item.strip()
        if ';q=' in item:
            lang, quality = item.split(';q=', 1)
            try:
                quality = float(quality)
            except ValueError:
                quality = 1.0
        else:
            lang = item
            quality = 1.0
        languages.append((lang.strip().lower(), quality))
    
    # Sort by quality (highest first)
    languages.sort(key=lambda x: x[1], reverse=True)
    
    # Find best matching language
    for lang_code, _ in languages:
        if lang_code in language_map:
            mapped_lang = language_map[lang_code]
            if is_supported_language(mapped_lang):
                return mapped_lang
        
        # Try base language (e.g., 'en' from 'en-US')
        base_lang = lang_code.split('-')[0]
        if base_lang in language_map:
            mapped_lang = language_map[base_lang]
            if is_supported_language(mapped_lang):
                return mapped_lang
    
    return None


def get_language_name(language_code):
    """
    Get the human-readable name for a language code
    """
    language_names = dict(settings.LANGUAGES)
    return language_names.get(language_code, 'Unknown')


def get_current_language():
    """Get the current active language code"""
    language = translation.get_language()
    
    # Map Django language codes to our data keys
    if language and language.startswith('id'):
        result = 'id'
    elif language and language.startswith('zh'):
        result = 'zh'
    elif language and language.startswith('es'):
        result = 'es'
    elif language and language.startswith('ja'):
        result = 'ja'
    elif language and language.startswith('pt'):
        result = 'pt'
    elif language and language.startswith('fr'):
        result = 'fr'
    elif language and language.startswith('de'):
        result = 'de'
    else:
        result = 'en'
    
    return result

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
        'is_german': current_lang == 'de',
        **base_data  # Spread base template data into context
    }
