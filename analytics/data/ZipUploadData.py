"""
ZIP Upload page content data for Indonesian and English localization
"""

ZIP_UPLOAD_DATA = {
    'en': {
        # Meta data
        'title': 'Upload ZIP File - Instagram Analytics',
        
        # Header
        'header_title': 'Upload ZIP File',
        'header_description': 'Upload your complete Instagram data export ZIP file. We\'ll automatically find and extract the followers and following data for analysis.',
        
        # Form
        'zip_file_label': 'Instagram Data ZIP File',
        'zip_file_description': 'Upload the complete ZIP file from your Instagram data export (containing following.json and followers_1.json)',
        'zip_file_placeholder': 'Click to upload or drag & drop',
        'submit_button': 'Analyze ZIP Data',
        
        # Help section
        'help_title': 'What we look for in your ZIP file:',
        'help_items': [
            'following.json - Contains your following list',
            'followers_1.json - Contains your followers list',
            'Files can be in any folder (commonly followers_and_following/)'
        ],
        'help_tutorial_text': 'Need help getting your data? View tutorial',
        
        # Alternative methods
        'alternative_methods': {
            'upload_files': {
                'title': 'Upload Individual Files',
                'description': 'Upload JSON files separately if you prefer more control.',
                'button': 'Upload Files'
            },
            'paste_data': {
                'title': 'Paste JSON Data',
                'description': 'Copy and paste your JSON data directly for quick analysis.',
                'button': 'Paste Data'
            }
        }
    },
    
    'id': {
        # Meta data
        'title': 'Unggah File ZIP - Analitik Instagram',
        
        # Header
        'header_title': 'Unggah File ZIP',
        'header_description': 'Unggah file ZIP ekspor data Instagram lengkap Anda. Kami akan secara otomatis menemukan dan mengekstrak data pengikut dan mengikuti untuk analisis.',
        
        # Form
        'zip_file_label': 'File ZIP Data Instagram',
        'zip_file_description': 'Unggah file ZIP lengkap dari ekspor data Instagram Anda (berisi following.json dan followers_1.json)',
        'zip_file_placeholder': 'Klik untuk mengunggah atau seret & lepas',
        'submit_button': 'Analisis Data ZIP',
        
        # Help section
        'help_title': 'Yang kami cari dalam file ZIP Anda:',
        'help_items': [
            'following.json - Berisi daftar mengikuti Anda',
            'followers_1.json - Berisi daftar pengikut Anda',
            'File dapat berada di folder mana pun (umumnya followers_and_following/)'
        ],
        'help_tutorial_text': 'Butuh bantuan mendapatkan data Anda? Lihat tutorial',
        
        # Alternative methods
        'alternative_methods': {
            'upload_files': {
                'title': 'Unggah File Individual',
                'description': 'Unggah file JSON secara terpisah jika Anda lebih suka kontrol lebih.',
                'button': 'Unggah File'
            },
            'paste_data': {
                'title': 'Tempel Data JSON',
                'description': 'Salin dan tempel data JSON Anda langsung untuk analisis cepat.',
                'button': 'Tempel Data'
            }
        }
    }
}
