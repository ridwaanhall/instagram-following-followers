"""
Base template content data for navigation and meta information
Contains both English and Indonesian translations
"""

BASE_DATA = {
    'en': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - Free Instagram Followers & Following Analyzer',
        'meta_description': 'Free Instagram analytics tool to analyze followers and following data. Find who doesn\'t follow back, mutual connections, and get insights about your Instagram network. No login required.',
        'meta_keywords': 'Instagram analytics, followers analyzer, following tracker, Instagram insights, social media analytics, Instagram tools, followers analysis, Instagram data, follower tracker, free Instagram tools',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Instagram Analytics Tool',
        
        # Additional SEO fields
        'meta_author': 'Ridwan Halim',
        'meta_robots': 'index, follow',
        'meta_theme_color': '#7c3aed',
        'meta_language': 'English',
        'og_type': 'website',
        'og_locale': 'en_US',
        'twitter_creator': '@ridwaanhall',
        'twitter_site': '@ridwaanhall',
        
        # Navigation
        'nav_brand': 'InstaAnalytics',
        'nav_home': 'Home',
        'nav_zip_upload': 'ZIP Upload',
        'nav_upload_files': 'Upload Files',
        'nav_text_input': 'Text Input',
        'nav_tutorial': 'Tutorial',
        
        # Language switcher
        'language_label': 'Language / Bahasa',
        'lang_english': 'English',
        'lang_indonesian': 'Indonesia',
        'lang_chinese': '中文',
        'lang_spanish': 'Español',
        'lang_japanese': '日本語',
        'lang_portuguese': 'Português',
        'lang_french': 'Français',
        
        # Footer
        'footer_brand': 'InstaAnalytics',
        'footer_created_by': 'Created with',
        'footer_by': 'by',
        'footer_creator_name': 'Ridwan Halim',
        'footer_built_with': 'Built with Django & Tailwind CSS',
        'footer_copyright': '© {% now \'Y\' %}',
        'footer_need_help': 'Need help?',
        
        # JSON-LD structured data
        'structured_data': {
            'name': 'InstaAnalytics',
            'description': 'Free Instagram analytics tool to analyze followers and following data. Find who doesn\'t follow back, mutual connections, and get insights about your Instagram network.',
            'keywords': 'Instagram analytics, followers analyzer, following tracker'
        },
        
        # Breadcrumb data for structured markup
        'breadcrumb_home': 'Home',
        'breadcrumb_analytics': 'Analytics',
        'breadcrumb_upload': 'Upload',
        'breadcrumb_tutorial': 'Tutorial'
    },
    'id': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - Analisis Pengikut & Mengikuti Instagram Gratis',
        'meta_description': 'Alat analisis Instagram gratis untuk menganalisis data pengikut dan mengikuti. Temukan siapa yang tidak mengikuti balik, koneksi bersama, dan dapatkan wawasan tentang jaringan Instagram Anda. Tidak perlu login.',
        'meta_keywords': 'analisis Instagram, penganalisis pengikut, pelacak mengikuti, wawasan Instagram, analisis media sosial, alat Instagram, analisis pengikut, data Instagram, pelacak pengikut, alat Instagram gratis',
        'site_name': 'InstaAnalytics',
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - Analisis Pengikut & Mengikuti Instagram Gratis',
        'meta_description': 'Alat analisis Instagram gratis untuk menganalisis data pengikut dan mengikuti. Temukan siapa yang tidak mengikuti balik, koneksi bersama, dan dapatkan wawasan tentang jaringan Instagram Anda. Tidak perlu login.',
        'meta_keywords': 'analisis Instagram, penganalisis pengikut, pelacak mengikuti, wawasan Instagram, analisis media sosial, alat Instagram, analisis pengikut, data Instagram, pelacak pengikut, alat Instagram gratis',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Alat Analisis Instagram',
        
        # Additional SEO fields
        'meta_author': 'Ridwan Halim',
        'meta_robots': 'index, follow',
        'meta_theme_color': '#7c3aed',
        'meta_language': 'Indonesian',
        'og_type': 'website',
        'og_locale': 'id_ID',
        'twitter_creator': '@ridwaanhall',
        'twitter_site': '@ridwaanhall',
        
        # Navigation
        'nav_brand': 'InstaAnalytics',
        'nav_home': 'Beranda',
        'nav_zip_upload': 'Unggah ZIP',
        'nav_upload_files': 'Unggah File',
        'nav_text_input': 'Input Teks',
        'nav_tutorial': 'Tutorial',
        
        # Language switcher
        'language_label': 'Language / Bahasa',
        'lang_english': 'English',
        'lang_indonesian': 'Indonesia',
        'lang_chinese': '中文',
        'lang_spanish': 'Español',
        'lang_japanese': '日本語',
        'lang_portuguese': 'Português',
        
        # Footer
        'footer_brand': 'InstaAnalytics',
        'footer_created_by': 'Dibuat dengan',
        'footer_by': 'oleh',
        'footer_creator_name': 'Ridwan Halim',
        'footer_built_with': 'Dibuat dengan Django & Tailwind CSS',
        'footer_copyright': '© {% now \'Y\' %}',
        'footer_need_help': 'Butuh bantuan?',
        
        # JSON-LD structured data
        'structured_data': {
            'name': 'InstaAnalytics',
            'description': 'Alat analisis Instagram gratis untuk menganalisis data pengikut dan mengikuti. Temukan siapa yang tidak mengikuti balik, koneksi bersama, dan dapatkan wawasan tentang jaringan Instagram Anda.',
            'keywords': 'analisis Instagram, penganalisis pengikut, pelacak mengikuti'
        },
        
        # Breadcrumb data for structured markup
        'breadcrumb_home': 'Beranda',
        'breadcrumb_analytics': 'Analitik',
        'breadcrumb_upload': 'Unggah',
        'breadcrumb_tutorial': 'Tutorial'
    },
    'zh': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - 免费Instagram粉丝和关注分析工具',
        'meta_description': '免费的Instagram分析工具，用于分析粉丝和关注数据。查找谁没有回关，互相关注的连接，获取Instagram网络洞察。无需登录。',
        'meta_keywords': 'Instagram分析, 粉丝分析器, 关注追踪器, Instagram洞察, 社交媒体分析, Instagram工具, 粉丝分析, Instagram数据, 粉丝追踪器, 免费Instagram工具',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Instagram分析工具',
        
        # Additional SEO fields
        'meta_author': 'Ridwan Halim',
        'meta_robots': 'index, follow',
        'meta_theme_color': '#7c3aed',
        'meta_language': 'Chinese',
        'og_type': 'website',
        'og_locale': 'zh_CN',
        'twitter_creator': '@ridwaanhall',
        'twitter_site': '@ridwaanhall',
        
        # Navigation
        'nav_brand': 'InstaAnalytics',
        'nav_home': '首页',
        'nav_zip_upload': 'ZIP上传',
        'nav_upload_files': '上传文件',
        'nav_text_input': '文本输入',
        'nav_tutorial': '教程',
        
        # Language switcher
        'language_label': 'Language / 语言',
        'lang_english': 'English',
        'lang_indonesian': 'Indonesia',
        'lang_chinese': '中文',
        'lang_spanish': 'Español',
        'lang_japanese': '日本語',
        'lang_portuguese': 'Português',
        
        # Footer
        'footer_brand': 'InstaAnalytics',
        'footer_created_by': '用爱制作',
        'footer_by': '由',
        'footer_creator_name': 'Ridwan Halim',
        'footer_built_with': '使用Django和Tailwind CSS构建',
        'footer_copyright': '© {% now \'Y\' %}',
        'footer_need_help': '需要帮助？',
        
        # JSON-LD structured data
        'structured_data': {
            'name': 'InstaAnalytics',
            'description': '免费的Instagram分析工具，用于分析粉丝和关注数据。查找谁没有回关，互相关注的连接，获取Instagram网络洞察。',
            'keywords': 'Instagram分析, 粉丝分析器, 关注追踪器'
        },
        
        # Breadcrumb data for structured markup
        'breadcrumb_home': '首页',
        'breadcrumb_analytics': '分析',
        'breadcrumb_upload': '上传',
        'breadcrumb_tutorial': '教程'
    },
    
    'es': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - Analizador Gratuito de Seguidores e Instagram',
        'meta_description': 'Herramienta gratuita de análisis de Instagram para analizar datos de seguidores y seguidos. Descubre quién no te sigue de vuelta, conexiones mutuas y obtén información sobre tu red de Instagram. No requiere inicio de sesión.',
        'meta_keywords': 'análisis Instagram, analizador seguidores, rastreador seguidos, insights Instagram, análisis redes sociales, herramientas Instagram, análisis seguidores, datos Instagram, rastreador seguidores, herramientas Instagram gratis',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Herramienta de Análisis de Instagram',
        
        # Additional SEO fields
        'meta_author': 'Ridwan Halim',
        'meta_robots': 'index, follow',
        'meta_theme_color': '#7c3aed',
        'meta_language': 'Spanish',
        'og_type': 'website',
        'og_locale': 'es_ES',
        'twitter_creator': '@ridwaanhall',
        'twitter_site': '@ridwaanhall',
        
        # Navigation
        'nav_brand': 'InstaAnalytics',
        'nav_home': 'Inicio',
        'nav_zip_upload': 'Subir ZIP',
        'nav_upload_files': 'Subir Archivos',
        'nav_text_input': 'Entrada de Texto',
        'nav_tutorial': 'Tutorial',
        
        # Language switcher
        'language_label': 'Idioma / Language',
        'lang_english': 'English',
        'lang_indonesian': 'Indonesia',
        'lang_chinese': '中文',
        'lang_spanish': 'Español',
        'lang_japanese': '日本語',
        'lang_portuguese': 'Português',
        'lang_french': 'Français',
        
        # Footer
        'footer_brand': 'InstaAnalytics',
        'footer_created_by': 'Creado con',
        'footer_by': 'por',
        'footer_creator_name': 'Ridwan Halim',
        'footer_built_with': 'Construido con Django y Tailwind CSS',
        'footer_copyright': '© {% now \'Y\' %}',
        'footer_need_help': '¿Necesitas ayuda?',
        
        # JSON-LD structured data
        'structured_data': {
            'name': 'InstaAnalytics',
            'description': 'Herramienta gratuita de análisis de Instagram para analizar datos de seguidores y seguidos. Descubre quién no te sigue de vuelta, conexiones mutuas y obtén información sobre tu red de Instagram.',
            'keywords': 'análisis Instagram, analizador seguidores, rastreador seguidos'
        },
        
        # Breadcrumb data for structured markup
        'breadcrumb_home': 'Inicio',
        'breadcrumb_analytics': 'Análisis',
        'breadcrumb_upload': 'Subir',
        'breadcrumb_tutorial': 'Tutorial'
    },
    
    'ja': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - 無料のInstagramフォロワー・フォロー分析ツール',
        'meta_description': '無料のInstagram分析ツールでフォロワーとフォローデータを分析。フォローバックしていない人、相互フォロー、Instagramネットワークの洞察を発見。ログイン不要。',
        'meta_keywords': 'Instagram分析, フォロワー分析, フォロー追跡, Instagramインサイト, ソーシャルメディア分析, Instagramツール, フォロワー解析, Instagramデータ, フォロワー追跡, 無料Instagramツール',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Instagram分析ツール',
        
        # Additional SEO fields
        'meta_author': 'Ridwan Halim',
        'meta_robots': 'index, follow',
        'meta_theme_color': '#7c3aed',
        'meta_language': 'Japanese',
        'og_type': 'website',
        'og_locale': 'ja_JP',
        'twitter_creator': '@ridwaanhall',
        'twitter_site': '@ridwaanhall',
        
        # Navigation
        'nav_brand': 'InstaAnalytics',
        'nav_home': 'ホーム',
        'nav_zip_upload': 'ZIPアップロード',
        'nav_upload_files': 'ファイルアップロード',
        'nav_text_input': 'テキスト入力',
        'nav_tutorial': 'チュートリアル',
        
        # Language switcher
        'language_label': '言語 / Language',
        'lang_english': 'English',
        'lang_indonesian': 'Indonesia',
        'lang_chinese': '中文',
        'lang_spanish': 'Español',
        'lang_japanese': '日本語',
        'lang_portuguese': 'Português',
        'lang_french': 'Français',
        
        # Footer
        'footer_brand': 'InstaAnalytics',
        'footer_created_by': '愛をこめて作成',
        'footer_by': 'by',
        'footer_creator_name': 'Ridwan Halim',
        'footer_built_with': 'Django & Tailwind CSSで構築',
        'footer_copyright': '© {% now \'Y\' %}',
        'footer_need_help': 'ヘルプが必要ですか？',
        
        # JSON-LD structured data
        'structured_data': {
            'name': 'InstaAnalytics',
            'description': '無料のInstagram分析ツールでフォロワーとフォローデータを分析。フォローバックしていない人、相互フォロー、Instagramネットワークの洞察を発見。',
            'keywords': 'Instagram分析, フォロワー分析, フォロー追跡'
        },
        
        # Breadcrumb data for structured markup
        'breadcrumb_home': 'ホーム',
        'breadcrumb_analytics': '分析',
        'breadcrumb_upload': 'アップロード',
        'breadcrumb_tutorial': 'チュートリアル'
    },
    
    'pt': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - Analisador Gratuito de Seguidores do Instagram',
        'meta_description': 'Ferramenta gratuita de análise do Instagram para analisar dados de seguidores e seguindo. Descubra quem não te segue de volta, conexões mútuas e insights sobre sua rede do Instagram. Não requer login.',
        'meta_keywords': 'análise Instagram, analisador seguidores, tracker seguindo, insights Instagram, análise redes sociais, ferramentas Instagram, análise seguidores, dados Instagram, tracker seguidores, ferramentas Instagram grátis',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Ferramenta de Análise do Instagram',
        
        # Additional SEO fields
        'meta_author': 'Ridwan Halim',
        'meta_robots': 'index, follow',
        'meta_theme_color': '#7c3aed',
        'meta_language': 'Portuguese',
        'og_type': 'website',
        'og_locale': 'pt_BR',
        'twitter_creator': '@ridwaanhall',
        'twitter_site': '@ridwaanhall',
        
        # Navigation
        'nav_brand': 'InstaAnalytics',
        'nav_home': 'Início',
        'nav_zip_upload': 'Upload ZIP',
        'nav_upload_files': 'Upload Arquivos',
        'nav_text_input': 'Entrada de Texto',
        'nav_tutorial': 'Tutorial',
        
        # Language switcher
        'language_label': 'Idioma / Language',
        'lang_english': 'English',
        'lang_indonesian': 'Indonesia',
        'lang_chinese': '中文',
        'lang_spanish': 'Español',
        'lang_japanese': '日本語',
        'lang_portuguese': 'Português',
        'lang_french': 'Français',
        
        # Footer
        'footer_brand': 'InstaAnalytics',
        'footer_created_by': 'Criado com',
        'footer_by': 'por',
        'footer_creator_name': 'Ridwan Halim',
        'footer_built_with': 'Construído com Django & Tailwind CSS',
        'footer_copyright': '© {% now \'Y\' %}',
        'footer_need_help': 'Precisa de ajuda?',
        
        # JSON-LD structured data
        'structured_data': {
            'name': 'InstaAnalytics',
            'description': 'Ferramenta gratuita de análise do Instagram para analisar dados de seguidores e seguindo. Descubra quem não te segue de volta, conexões mútuas e insights sobre sua rede do Instagram.',
            'keywords': 'análise Instagram, analisador seguidores, tracker seguindo'
        },
        
        # Breadcrumb data for structured markup
        'breadcrumb_home': 'Início',
        'breadcrumb_analytics': 'Análise',
        'breadcrumb_upload': 'Upload',
        'breadcrumb_tutorial': 'Tutorial'
    },
    
    'fr': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - Outil Gratuit d\'Analyse des Abonnés Instagram',
        'meta_description': 'Outil d\'analyse Instagram gratuit pour analyser les données d\'abonnés et d\'abonnements. Découvrez qui ne vous suit pas en retour, les connexions mutuelles, et obtenez des insights sur votre réseau Instagram. Aucune connexion requise.',
        'meta_keywords': 'analyse Instagram, analyseur abonnés, tracker abonnements, insights Instagram, analyse réseaux sociaux, outil Instagram, analyse followers, données Instagram, tracker abonnés, outil Instagram gratuit',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Outil d\'Analyse Instagram',
        
        # Additional SEO fields
        'meta_author': 'Ridwan Halim',
        'meta_robots': 'index, follow',
        'meta_theme_color': '#7c3aed',
        'meta_language': 'French',
        'og_type': 'website',
        'og_locale': 'fr_FR',
        'twitter_creator': '@ridwaanhall',
        'twitter_site': '@ridwaanhall',
        
        # Navigation
        'nav_brand': 'InstaAnalytics',
        'nav_home': 'Accueil',
        'nav_zip_upload': 'Upload ZIP',
        'nav_upload_files': 'Upload Fichiers',
        'nav_text_input': 'Saisie Texte',
        'nav_tutorial': 'Tutoriel',
        
        # Language switcher
        'language_label': 'Langue / Language',
        'lang_english': 'English',
        'lang_indonesian': 'Indonesia',
        'lang_chinese': '中文',
        'lang_spanish': 'Español',
        'lang_japanese': '日本語',
        'lang_portuguese': 'Português',
        'lang_french': 'Français',
        
        # Footer
        'footer_brand': 'InstaAnalytics',
        'footer_created_by': 'Créé avec',
        'footer_by': 'par',
        'footer_creator_name': 'Ridwan Halim',
        'footer_built_with': 'Construit avec Django & Tailwind CSS',
        'footer_copyright': '© {% now \'Y\' %}',
        'footer_need_help': 'Besoin d\'aide ?',
        
        # Schema.org structured data
        'schema_site_name': 'InstaAnalytics',
        'schema_description': 'Outil d\'analyse Instagram gratuit pour analyser vos abonnés et abonnements avec des insights détaillés',
        'schema_publisher': 'InstaAnalytics',
        'schema_author': 'Ridwan Halim',
        'schema_logo_alt': 'Logo InstaAnalytics',
        'schema_image_caption': 'Interface de l\'outil d\'analyse Instagram InstaAnalytics',
        
        # Breadcrumb data for structured markup
        'breadcrumb_home': 'Accueil',
        'breadcrumb_analytics': 'Analyse',
        'breadcrumb_upload': 'Upload',
        'breadcrumb_tutorial': 'Tutoriel'
    }
}
