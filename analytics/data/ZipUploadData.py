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
    },
    
    'zh': {
        # Meta data
        'title': '上传ZIP文件 - Instagram分析',
        
        # Header
        'header_title': '上传ZIP文件',
        'header_description': '上传您完整的Instagram数据导出ZIP文件。我们将自动查找并提取粉丝和关注数据进行分析。',
        
        # Form
        'zip_file_label': 'Instagram数据ZIP文件',
        'zip_file_description': '上传您Instagram数据导出的完整ZIP文件（包含following.json和followers_1.json）',
        'zip_file_placeholder': '点击上传或拖放',
        'submit_button': '分析ZIP数据',
        
        # Help section
        'help_title': '我们在您的ZIP文件中查找的内容：',
        'help_items': [
            'following.json - 包含您的关注列表',
            'followers_1.json - 包含您的粉丝列表',
            '文件可以在任何文件夹中（通常在followers_and_following/）'
        ],
        'help_tutorial_text': '需要帮助获取您的数据？查看教程',
        
        # Alternative methods
        'alternative_methods': {
            'upload_files': {
                'title': '上传单个文件',
                'description': '如果您更喜欢更多控制权，可以单独上传JSON文件。',
                'button': '上传文件'
            },
            'paste_data': {
                'title': '粘贴JSON数据',
                'description': '直接复制粘贴您的JSON数据进行快速分析。',
                'button': '粘贴数据'
            }
        }
    }
}
