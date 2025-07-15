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
        }
    },
    'id': {
        # Meta tags and SEO
        'site_title': 'InstaAnalytics - Analisis Pengikut & Mengikuti Instagram Gratis',
        'meta_description': 'Alat analisis Instagram gratis untuk menganalisis data pengikut dan mengikuti. Temukan siapa yang tidak mengikuti balik, koneksi bersama, dan dapatkan wawasan tentang jaringan Instagram Anda. Tidak perlu login.',
        'meta_keywords': 'analisis Instagram, penganalisis pengikut, pelacak mengikuti, wawasan Instagram, analisis media sosial, alat Instagram, analisis pengikut, data Instagram, pelacak pengikut, alat Instagram gratis',
        'site_name': 'InstaAnalytics',
        'og_image_alt': 'InstaAnalytics - Alat Analisis Instagram',
        
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
        }
    }
}
