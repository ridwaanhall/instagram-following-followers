"""
Management command to check language detection and localization setup
"""

from django.core.management.base import BaseCommand
from django.conf import settings
from analytics.utils import get_language_info, is_supported_language
from analytics.data.HomeData import HOME_DATA
from analytics.data.BaseData import BASE_DATA


class Command(BaseCommand):
    help = 'Check language detection and localization setup'

    def add_arguments(self, parser):
        parser.add_argument(
            '--test-browser-lang',
            type=str,
            help='Test browser language detection with a specific Accept-Language header',
        )
        parser.add_argument(
            '--check-data',
            action='store_true',
            help='Check if all languages have complete data',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Language Detection & Localization Status'))
        self.stdout.write('=' * 50)
        
        # Display current language configuration
        lang_info = get_language_info()
        self.stdout.write(f"Current language: {lang_info['current']} ({lang_info['current_name']})")
        self.stdout.write(f"Supported languages: {len(lang_info['available'])}")
        
        for code, name in lang_info['available'].items():
            self.stdout.write(f"  - {code}: {name}")
        
        # Run automatic browser language tests
        self.stdout.write("\n" + "="*50)
        self.stdout.write("Testing Browser Language Detection")
        self.stdout.write("="*50)
        self._run_browser_tests()
        
        # Test browser language detection if requested
        if options['test_browser_lang']:
            self._test_browser_language(options['test_browser_lang'])
        
        # Check data completeness if requested
        if options['check_data']:
            self._check_data_completeness()

    def _run_browser_tests(self):
        """Run comprehensive browser language detection tests"""
        test_cases = [
            ('en-US,en;q=0.9', 'English (US)'),
            ('id-ID,id;q=0.9,en;q=0.8', 'Indonesian'),
            ('zh-CN,zh;q=0.9,en;q=0.8', 'Chinese (Simplified)'),
            ('es-ES,es;q=0.9,en;q=0.8', 'Spanish'),
            ('ja-JP,ja;q=0.9,en;q=0.8', 'Japanese'),
            ('pt-BR,pt;q=0.9,en;q=0.8', 'Portuguese (Brazil)'),
            ('fr-FR,fr;q=0.9,en;q=0.8', 'French'),
            ('de-DE,de;q=0.9,en;q=0.8', 'German'),
            ('ko-KR,ko;q=0.9,en;q=0.8', 'Korean (fallback to English)'),
            ('zh-TW,zh;q=0.9,en;q=0.8', 'Chinese (Traditional -> Simplified)'),
        ]
        
        # Import here to avoid circular imports
        from django.test import RequestFactory
        from analytics.utils import detect_language_from_browser_header
        
        factory = RequestFactory()
        
        for accept_lang, description in test_cases:
            # Create a mock request with the Accept-Language header
            request = factory.get('/')
            request.META['HTTP_ACCEPT_LANGUAGE'] = accept_lang
            
            detected = detect_language_from_browser_header(request)
            status = "✓" if detected else "✗"
            result = detected or "None (fallback to default)"
            
            self.stdout.write(f"{status} {accept_lang:<30} -> {result:<10} ({description})")

    def _test_browser_language(self, accept_language):
        """Test browser language detection with a specific Accept-Language header"""
        self.stdout.write('\n' + self.style.WARNING('Testing Browser Language Detection'))
        self.stdout.write('-' * 40)
        self.stdout.write(f"Accept-Language: {accept_language}")
        
        # Simulate request-like parsing
        from analytics.middleware import AutoLanguageDetectionMiddleware
        middleware = AutoLanguageDetectionMiddleware()
        languages = middleware._parse_accept_language(accept_language)
        
        self.stdout.write("Parsed languages (by preference):")
        for lang, quality in languages:
            self.stdout.write(f"  {lang} (q={quality})")
        
        # Test mapping
        for lang, quality in languages:
            if lang.lower() in middleware.LANGUAGE_MAP:
                mapped = middleware.LANGUAGE_MAP[lang.lower()]
                supported = is_supported_language(mapped)
                status = "✓ Supported" if supported else "✗ Not supported"
                self.stdout.write(f"  {lang} → {mapped} ({status})")

    def _check_data_completeness(self):
        """Check if all supported languages have complete data"""
        self.stdout.write('\n' + self.style.WARNING('Data Completeness Check'))
        self.stdout.write('-' * 30)
        
        supported_langs = [lang[0] for lang in settings.LANGUAGES]
        data_sources = {
            'HomeData': HOME_DATA,
            'BaseData': BASE_DATA,
        }
        
        for data_name, data_dict in data_sources.items():
            self.stdout.write(f"\n{data_name}:")
            for lang_code in supported_langs:
                if lang_code in data_dict:
                    # Convert Django language codes to our data keys
                    data_key = self._get_data_key(lang_code)
                    if data_key in data_dict:
                        self.stdout.write(f"  ✓ {lang_code} ({data_key})")
                    else:
                        self.stdout.write(self.style.ERROR(f"  ✗ {lang_code} ({data_key}) - Missing"))
                else:
                    data_key = self._get_data_key(lang_code)
                    if data_key in data_dict:
                        self.stdout.write(f"  ✓ {lang_code} ({data_key})")
                    else:
                        self.stdout.write(self.style.ERROR(f"  ✗ {lang_code} ({data_key}) - Missing"))

    def _get_data_key(self, django_lang_code):
        """Convert Django language code to our data key format"""
        mapping = {
            'en': 'en',
            'id': 'id',
            'zh-hans': 'zh',
            'es': 'es',
            'ja': 'ja',
            'pt-br': 'pt',
            'fr': 'fr',
            'de': 'de',
        }
        return mapping.get(django_lang_code, django_lang_code)
