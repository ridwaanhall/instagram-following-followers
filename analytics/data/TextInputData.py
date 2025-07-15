"""
Text Input page content data for Indonesian and English localization
"""

TEXT_INPUT_DATA = {
    'en': {
        # Meta data
        'title': 'Paste JSON Data - Instagram Analytics',
        
        # Header
        'header_title': 'Paste JSON Data',
        'header_description': 'Copy and paste your Instagram JSON data directly for quick analysis',
        
        # Form labels
        'following_label': 'Following JSON Data',
        'followers_label': 'Followers JSON Data',
        
        # Placeholders
        'following_placeholder': '''Paste your following.json content here...

Example:
{
  "relationships_following": [
    {
      "string_list_data": [
        {
          "href": "...",
          "value": "username1",
          "timestamp": 1234567890
        }
      ]
    }
  ]
}''',
        
        'followers_placeholder': '''Paste your followers_1.json content here...

Example:
[
  {
    "string_list_data": [
      {
        "href": "...",
        "value": "follower1",
        "timestamp": 1234567890
      }
    ]
  }
]''',
        
        # Descriptions
        'following_description': 'Paste the complete content from your "following.json" file',
        'followers_description': 'Paste the complete content from your "followers_1.json" file',
        
        # Validation
        'validation_waiting': 'JSON validation: Waiting for input',
        'validation_valid': 'JSON validation: Valid JSON format ✓',
        'validation_invalid': 'JSON validation: Invalid JSON format ✗',
        
        # Submit button
        'submit_button': 'Analyze JSON Data',
        
        # Help sections
        'json_help': {
            'title': 'JSON Format Help',
            'description': 'Make sure your JSON data follows the correct Instagram export format. The system will validate your input automatically.',
            'format_example': '''following.json: {"relationships_following": [...]}
followers_1.json: [{"string_list_data": [...]}]'''
        },
        
        'tutorial_help': {
            'title': 'Need Help Getting Your Data?',
            'description': 'Our step-by-step tutorial will guide you through downloading your Instagram data export.',
            'button': 'View Tutorial'
        }
    },
    
    'id': {
        # Meta data
        'title': 'Tempel Data JSON - Analitik Instagram',
        
        # Header
        'header_title': 'Tempel Data JSON',
        'header_description': 'Salin dan tempel data JSON Instagram Anda langsung untuk analisis cepat',
        
        # Form labels
        'following_label': 'Data JSON Mengikuti',
        'followers_label': 'Data JSON Pengikut',
        
        # Placeholders
        'following_placeholder': '''Tempel konten following.json Anda di sini...

Contoh:
{
  "relationships_following": [
    {
      "string_list_data": [
        {
          "href": "...",
          "value": "username1",
          "timestamp": 1234567890
        }
      ]
    }
  ]
}''',
        
        'followers_placeholder': '''Tempel konten followers_1.json Anda di sini...

Contoh:
[
  {
    "string_list_data": [
      {
        "href": "...",
        "value": "follower1",
        "timestamp": 1234567890
      }
    ]
  }
]''',
        
        # Descriptions
        'following_description': 'Tempel konten lengkap dari file "following.json" Anda',
        'followers_description': 'Tempel konten lengkap dari file "followers_1.json" Anda',
        
        # Validation
        'validation_waiting': 'Validasi JSON: Menunggu input',
        'validation_valid': 'Validasi JSON: Format JSON valid ✓',
        'validation_invalid': 'Validasi JSON: Format JSON tidak valid ✗',
        
        # Submit button
        'submit_button': 'Analisis Data JSON',
        
        # Help sections
        'json_help': {
            'title': 'Bantuan Format JSON',
            'description': 'Pastikan data JSON Anda mengikuti format ekspor Instagram yang benar. Sistem akan memvalidasi input Anda secara otomatis.',
            'format_example': '''following.json: {"relationships_following": [...]}
followers_1.json: [{"string_list_data": [...]}]'''
        },
        
        'tutorial_help': {
            'title': 'Butuh Bantuan Mendapatkan Data Anda?',
            'description': 'Tutorial langkah demi langkah kami akan memandu Anda melalui pengunduhan ekspor data Instagram.',
            'button': 'Lihat Tutorial'
        }
    }
}
