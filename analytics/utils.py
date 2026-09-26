"""
Language detection and per-language content lookup.
"""

from django.conf import settings
from django.utils import translation

from .data.BaseData import BASE_DATA
from .data.HomeData import HOME_DATA
from .data.PrivacyData import PRIVACY_DATA
from .data.ResultsData import RESULTS_DATA
from .data.TermsData import TERMS_DATA
from .data.TextInputData import TEXT_INPUT_DATA
from .data.TutorialData import TUTORIAL_DATA
from .data.UiData import UI_DATA
from .data.UploadData import UPLOAD_DATA
from .data.ZipUploadData import ZIP_UPLOAD_DATA

# Browser language tag -> Django language code. Region-less tags cover the
# rest, because unknown regions fall back to their base language.
BROWSER_LANGUAGE_MAP = {
    'en': 'en',
    'id': 'id',
    'zh': 'zh-hans', 'zh-cn': 'zh-hans', 'zh-hans': 'zh-hans', 'zh-sg': 'zh-hans', 'zh-my': 'zh-hans',
    'es': 'es',
    'ja': 'ja',
    'pt': 'pt-br', 'pt-br': 'pt-br', 'pt-pt': 'pt-br',
    'fr': 'fr',
    'de': 'de',
}

# Language picker entries: (Django code, content key, native name).
LANGUAGE_CHOICES = [
    ('en', 'en', 'English'),
    ('id', 'id', 'Bahasa Indonesia'),
    ('zh-hans', 'zh', '中文'),
    ('es', 'es', 'Español'),
    ('ja', 'ja', '日本語'),
    ('pt-br', 'pt', 'Português'),
    ('fr', 'fr', 'Français'),
]


def is_supported_language(language_code):
    return language_code in dict(settings.LANGUAGES)


def get_language_info():
    current_lang = get_current_language()
    return {
        'current': current_lang,
        'current_name': dict(settings.LANGUAGES).get(current_lang, current_lang),
        'available': dict(settings.LANGUAGES),
        'supported_codes': [code for code, _ in settings.LANGUAGES],
    }


def parse_accept_language(header):
    """``Accept-Language`` -> list of lowercase tags, best first."""
    languages = []
    for item in header.split(','):
        lang, _, quality = item.strip().partition(';q=')
        try:
            q = float(quality) if quality else 1.0
        except ValueError:
            q = 1.0
        if lang:
            languages.append((lang.strip().lower(), q))
    return [lang for lang, _ in sorted(languages, key=lambda x: x[1], reverse=True)]


def detect_language_from_browser_header(request):
    """Best supported language from ``Accept-Language``, or None."""
    for tag in parse_accept_language(request.META.get('HTTP_ACCEPT_LANGUAGE', '')):
        for candidate in (tag, tag.split('-')[0]):
            mapped = BROWSER_LANGUAGE_MAP.get(candidate)
            if mapped and is_supported_language(mapped):
                return mapped
    return None


def detect_language_from_request(request):
    """URL parameter > session > browser header > default."""
    lang_param = request.GET.get('lang') or request.POST.get('lang')
    if lang_param and is_supported_language(lang_param):
        return lang_param
    session_lang = request.session.get(settings.LANGUAGE_SESSION_KEY)
    if session_lang and is_supported_language(session_lang):
        return session_lang
    return detect_language_from_browser_header(request) or settings.LANGUAGE_CODE


def get_current_language():
    """Active Django language mapped to a content key (``zh-hans`` -> ``zh``)."""
    language = (translation.get_language() or 'en').split('-')[0]
    return language if language in {'id', 'zh', 'es', 'ja', 'pt', 'fr', 'de'} else 'en'


def get_content_data(data_dict, language=None):
    """Content for ``language``, falling back to English."""
    return data_dict.get(language or get_current_language(), data_dict['en'])


def get_home_data(language=None):
    return get_content_data(HOME_DATA, language)


def get_upload_data(language=None):
    return get_content_data(UPLOAD_DATA, language)


def get_zip_upload_data(language=None):
    return get_content_data(ZIP_UPLOAD_DATA, language)


def get_text_input_data(language=None):
    return get_content_data(TEXT_INPUT_DATA, language)


def get_tutorial_data(language=None):
    return get_content_data(TUTORIAL_DATA, language)


def get_results_data(language=None):
    return get_content_data(RESULTS_DATA, language)


def get_base_data(language=None):
    return get_content_data(BASE_DATA, language)


def get_analyzer_data(language=None):
    """Strings for the three-tab analyzer shown on home and every method page."""
    return {
        'az': get_zip_upload_data(language),
        'af': get_upload_data(language),
        'at': get_text_input_data(language),
    }


def get_privacy_data(language=None):
    """Privacy notice content.

    Deliberately not language-switched: the notice states one authoritative
    English version rather than seven machine-translated approximations of a
    legal document. The `language` argument exists only so callers can treat
    this like every other content getter.
    """
    return PRIVACY_DATA


def get_terms_data(language=None):
    """Terms of use. English only, like the privacy notice."""
    return TERMS_DATA


def inject_i18n_context(request):
    """Context processor: base-template strings plus language picker data."""
    current_lang = get_current_language()
    return {
        'current_language': current_lang,
        'html_lang': {'zh': 'zh-Hans', 'pt': 'pt-BR'}.get(current_lang, current_lang),
        'language_choices': [
            {'code': code, 'name': name, 'active': key == current_lang}
            for code, key, name in LANGUAGE_CHOICES
        ],
        **get_base_data(current_lang),
        **get_content_data(UI_DATA, current_lang),
    }
