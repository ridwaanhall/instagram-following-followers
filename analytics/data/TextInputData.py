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
    },
    
    'zh': {
        # Meta data
        'title': '粘贴JSON数据 - Instagram分析',
        
        # Header
        'header_title': '粘贴JSON数据',
        'header_description': '直接复制粘贴您的Instagram JSON数据进行快速分析',
        
        # Form labels
        'following_label': '关注JSON数据',
        'followers_label': '粉丝JSON数据',
        
        # Placeholders
        'following_placeholder': '''在此粘贴您的following.json内容...

示例:
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
        
        'followers_placeholder': '''在此粘贴您的followers_1.json内容...

示例:
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
        'following_description': '粘贴您"following.json"文件的完整内容',
        'followers_description': '粘贴您"followers_1.json"文件的完整内容',
        
        # Validation
        'validation_waiting': 'JSON验证：等待输入',
        'validation_valid': 'JSON验证：有效的JSON格式 ✓',
        'validation_invalid': 'JSON验证：无效的JSON格式 ✗',
        
        # Submit button
        'submit_button': '分析JSON数据',
        
        # Help sections
        'json_help': {
            'title': 'JSON格式帮助',
            'description': '确保您的JSON数据遵循正确的Instagram导出格式。系统将自动验证您的输入。',
            'format_example': '''following.json: {"relationships_following": [...]}
followers_1.json: [{"string_list_data": [...]}]'''
        },
        
        'tutorial_help': {
            'title': '需要帮助获取您的数据？',
            'description': '我们的分步教程将指导您下载Instagram数据导出。',
            'button': '查看教程'
        }
    }
}
