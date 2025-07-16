"""
Custom middleware for automatic language detection based on browser language and region
"""

import re
from django.utils import translation
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class AutoLanguageDetectionMiddleware(MiddlewareMixin):
    """
    Middleware to automatically detect and set language based on:
    1. URL language prefix (if present)
    2. User session preference
    3. Browser Accept-Language header
    4. Fallback to default language
    """
    
    # Language mapping from browser language codes to our supported languages
    LANGUAGE_MAP = {
        # English variants
        'en': 'en',
        'en-us': 'en',
        'en-gb': 'en',
        'en-au': 'en',
        'en-ca': 'en',
        
        # Indonesian
        'id': 'id',
        'id-id': 'id',
        
        # Chinese variants
        'zh': 'zh-hans',
        'zh-cn': 'zh-hans',
        'zh-hans': 'zh-hans',
        'zh-sg': 'zh-hans',
        'zh-my': 'zh-hans',
        
        # Spanish variants
        'es': 'es',
        'es-es': 'es',
        'es-mx': 'es',
        'es-ar': 'es',
        'es-co': 'es',
        'es-cl': 'es',
        'es-pe': 'es',
        'es-ve': 'es',
        
        # Japanese
        'ja': 'ja',
        'ja-jp': 'ja',
        
        # Portuguese variants
        'pt': 'pt-br',
        'pt-br': 'pt-br',
        'pt-pt': 'pt-br',  # We use Brazilian Portuguese as default
        
        # French variants
        'fr': 'fr',
        'fr-fr': 'fr',
        'fr-ca': 'fr',
        'fr-be': 'fr',
        'fr-ch': 'fr',
        
        # German variants
        'de': 'de',
        'de-de': 'de',
        'de-at': 'de',  # Austria
        'de-ch': 'de',  # Switzerland
    }

    def process_request(self, request):
        """
        Process the request to determine the appropriate language
        """
        # Skip language detection for admin, API, or static URLs
        if self._should_skip_language_detection(request):
            return None
            
        # Check if language is explicitly set in session (user choice)
        # This should take priority over browser detection
        session_language = request.session.get(settings.LANGUAGE_SESSION_KEY)
        if session_language and self._is_supported_language(session_language):
            translation.activate(session_language)
            request.LANGUAGE_CODE = session_language
            return None
        
        # Check for URL parameter (highest priority for this request)
        lang_param = request.GET.get('lang') or request.POST.get('lang')
        if lang_param and self._is_supported_language(lang_param):
            translation.activate(lang_param)
            request.LANGUAGE_CODE = lang_param
            request.session[settings.LANGUAGE_SESSION_KEY] = lang_param
            return None
        
        # Fallback to browser language detection only if no session preference exists
        detected_language = self._detect_language_from_browser(request)
        if detected_language:
            translation.activate(detected_language)
            request.LANGUAGE_CODE = detected_language
            # Only set in session if no explicit preference exists
            if not request.session.get(settings.LANGUAGE_SESSION_KEY):
                request.session[settings.LANGUAGE_SESSION_KEY] = detected_language
        
        return None

    def _should_skip_language_detection(self, request):
        """
        Check if we should skip language detection for this request
        """
        path = request.path_info
        
        # Skip for admin, static files, media files, and API endpoints
        skip_patterns = [
            '/admin/',
            '/static/',
            '/media/',
            '/api/',
            '/favicon.ico',
            '/robots.txt',
            '/sitemap.xml',
        ]
        
        return any(path.startswith(pattern) for pattern in skip_patterns)

    def _detect_language_from_browser(self, request):
        """
        Detect language from browser Accept-Language header
        """
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
        if not accept_language:
            return settings.LANGUAGE_CODE
        
        # Parse Accept-Language header
        languages = self._parse_accept_language(accept_language)
        
        # Find the best matching language
        for lang_code, quality in languages:
            # Try exact match first
            if lang_code.lower() in self.LANGUAGE_MAP:
                mapped_language = self.LANGUAGE_MAP[lang_code.lower()]
                if self._is_supported_language(mapped_language):
                    return mapped_language
            
            # Try partial match (e.g., 'en' from 'en-US')
            base_lang = lang_code.split('-')[0].lower()
            if base_lang in self.LANGUAGE_MAP:
                mapped_language = self.LANGUAGE_MAP[base_lang]
                if self._is_supported_language(mapped_language):
                    return mapped_language
        
        # Fallback to default language
        return settings.LANGUAGE_CODE

    def _parse_accept_language(self, accept_language):
        """
        Parse the Accept-Language header and return sorted list of (language, quality)
        """
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
            
            languages.append((lang.strip(), quality))
        
        # Sort by quality (highest first)
        return sorted(languages, key=lambda x: x[1], reverse=True)

    def _is_supported_language(self, language_code):
        """
        Check if the language code is supported by our application
        """
        supported_languages = [lang[0] for lang in settings.LANGUAGES]
        return language_code in supported_languages


class GeolocationLanguageMiddleware(MiddlewareMixin):
    """
    Optional middleware for geolocation-based language detection
    This can be used in addition to browser language detection
    """
    
    # Country to language mapping for better regional targeting
    COUNTRY_LANGUAGE_MAP = {
        # English-speaking countries
        'US': 'en', 'GB': 'en', 'AU': 'en', 'CA': 'en', 'NZ': 'en', 'IE': 'en',
        
        # Indonesian-speaking countries
        'ID': 'id',
        
        # Chinese-speaking countries/regions
        'CN': 'zh-hans', 'SG': 'zh-hans', 'MY': 'zh-hans',
        
        # Spanish-speaking countries
        'ES': 'es', 'MX': 'es', 'AR': 'es', 'CO': 'es', 'CL': 'es', 'PE': 'es',
        'VE': 'es', 'EC': 'es', 'BO': 'es', 'PY': 'es', 'UY': 'es', 'CR': 'es',
        'PA': 'es', 'GT': 'es', 'HN': 'es', 'SV': 'es', 'NI': 'es', 'DO': 'es',
        'CU': 'es', 'PR': 'es',
        
        # Japanese-speaking countries
        'JP': 'ja',
        
        # Portuguese-speaking countries
        'BR': 'pt-br', 'PT': 'pt-br',
        
        # French-speaking countries
        'FR': 'fr', 'BE': 'fr', 'CH': 'fr', 'CA': 'fr',
        
        # German-speaking countries
        'DE': 'de', 'AT': 'de', 'CH': 'de',
    }

    def process_request(self, request):
        """
        Process request for geolocation-based language detection
        Note: This requires the country code to be available in request
        (e.g., from CloudFlare, AWS CloudFront, or other CDN headers)
        """
        # Skip if language is already set or if we should skip detection
        if hasattr(request, 'LANGUAGE_CODE') or self._should_skip_language_detection(request):
            return None
        
        # Try to get country code from various headers
        country_code = self._get_country_code(request)
        
        if country_code and country_code in self.COUNTRY_LANGUAGE_MAP:
            detected_language = self.COUNTRY_LANGUAGE_MAP[country_code]
            
            # Only set if we don't have a language preference yet
            if not request.session.get(settings.LANGUAGE_SESSION_KEY):
                if self._is_supported_language(detected_language):
                    translation.activate(detected_language)
                    request.LANGUAGE_CODE = detected_language
                    request.session[settings.LANGUAGE_SESSION_KEY] = detected_language
        
        return None

    def _get_country_code(self, request):
        """
        Get country code from request headers
        Different CDN/proxy services use different headers
        """
        # Common headers used by CDNs and proxy services
        country_headers = [
            'HTTP_CF_IPCOUNTRY',        # CloudFlare
            'HTTP_X_COUNTRY_CODE',      # Generic
            'HTTP_X_FORWARDED_COUNTRY', # Some proxies
            'HTTP_CLOUDFRONT_VIEWER_COUNTRY', # AWS CloudFront
        ]
        
        for header in country_headers:
            country = request.META.get(header, '').upper()
            if country and len(country) == 2:  # Valid ISO country code
                return country
        
        return None

    def _should_skip_language_detection(self, request):
        """
        Same skip logic as AutoLanguageDetectionMiddleware
        """
        path = request.path_info
        skip_patterns = ['/admin/', '/static/', '/media/', '/api/', '/favicon.ico', '/robots.txt', '/sitemap.xml']
        return any(path.startswith(pattern) for pattern in skip_patterns)

    def _is_supported_language(self, language_code):
        """
        Check if the language code is supported by our application
        """
        supported_languages = [lang[0] for lang in settings.LANGUAGES]
        return language_code in supported_languages
