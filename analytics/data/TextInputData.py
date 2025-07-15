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
    },
    
    'es': {
        # Meta data
        'title': 'Pegar Datos JSON - Analytics de Instagram',
        
        # Header
        'header_title': 'Pegar Datos JSON',
        'header_description': 'Copia y pega tus datos JSON de Instagram directamente para análisis rápido',
        
        # Form labels
        'following_label': 'Datos JSON de Seguidos',
        'followers_label': 'Datos JSON de Seguidores',
        
        # Placeholders
        'following_placeholder': '''Pega el contenido de tu following.json aquí...

Ejemplo:
{
  "relationships_following": [
    {
      "string_list_data": [
        {
          "href": "...",
          "value": "usuario1",
          "timestamp": 1234567890
        }
      ]
    }
  ]
}''',
        
        'followers_placeholder': '''Pega el contenido de tu followers_1.json aquí...

Ejemplo:
[
  {
    "string_list_data": [
      {
        "href": "...",
        "value": "seguidor1",
        "timestamp": 1234567890
      }
    ]
  }
]''',
        
        # Descriptions
        'following_description': 'Pega el contenido completo de tu archivo "following.json"',
        'followers_description': 'Pega el contenido completo de tu archivo "followers_1.json"',
        
        # Validation
        'validation_waiting': 'Validación JSON: Esperando entrada',
        'validation_valid': 'Validación JSON: Formato JSON válido ✓',
        'validation_invalid': 'Validación JSON: Formato JSON inválido ✗',
        
        # Submit button
        'submit_button': 'Analizar Datos JSON',
        
        # Help sections
        'json_help': {
            'title': 'Ayuda con Formato JSON',
            'description': 'Asegúrate de que tus datos JSON sigan el formato correcto de exportación de Instagram. El sistema validará tu entrada automáticamente.',
            'format_example': '''following.json: {"relationships_following": [...]}
followers_1.json: [{"string_list_data": [...]}]'''
        },
        
        'tutorial_help': {
            'title': '¿Necesitas Ayuda para Obtener Tus Datos?',
            'description': 'Nuestro tutorial paso a paso te guiará a través de la descarga de tu exportación de datos de Instagram.',
            'button': 'Ver Tutorial'
        }
    },
    
    'ja': {
        # Meta data
        'title': 'JSONデータを貼り付け - Instagram分析',
        
        # Header
        'header_title': 'JSONデータを貼り付け',
        'header_description': 'InstagramのJSONデータを直接コピー&ペーストして迅速分析',
        
        # Form labels
        'following_label': 'フォローJSONデータ',
        'followers_label': 'フォロワーJSONデータ',
        
        # Placeholders
        'following_placeholder': '''following.jsonの内容をここに貼り付け...

例:
{
  "relationships_following": [
    {
      "string_list_data": [
        {
          "href": "...",
          "value": "ユーザー名1",
          "timestamp": 1234567890
        }
      ]
    }
  ]
}''',
        
        'followers_placeholder': '''followers_1.jsonの内容をここに貼り付け...

例:
[
  {
    "string_list_data": [
      {
        "href": "...",
        "value": "フォロワー1",
        "timestamp": 1234567890
      }
    ]
  }
]''',
        
        # Descriptions
        'following_description': '「following.json」ファイルの完全な内容を貼り付け',
        'followers_description': '「followers_1.json」ファイルの完全な内容を貼り付け',
        
        # Validation
        'validation_waiting': 'JSON検証: 入力待機中',
        'validation_valid': 'JSON検証: 有効なJSON形式 ✓',
        'validation_invalid': 'JSON検証: 無効なJSON形式 ✗',
        
        # Submit button
        'submit_button': 'JSONデータを分析',
        
        # Help sections
        'json_help': {
            'title': 'JSON形式ヘルプ',
            'description': 'JSONデータが正しいInstagramエクスポート形式に従っていることを確認してください。システムが入力を自動的に検証します。',
            'format_example': '''following.json: {"relationships_following": [...]}
followers_1.json: [{"string_list_data": [...]}]'''
        },
        
        'tutorial_help': {
            'title': 'データ取得でお困りですか？',
            'description': 'ステップバイステップのチュートリアルでInstagramデータエクスポートのダウンロードをガイドします。',
            'button': 'チュートリアルを見る'
        }
    },
    
    'pt': {
        # Meta data
        'title': 'Colar Dados JSON - Analytics Instagram',
        
        # Header
        'header_title': 'Colar Dados JSON',
        'header_description': 'Copie e cole seus dados JSON do Instagram diretamente para análise rápida',
        
        # Form labels
        'following_label': 'Dados JSON de Seguindo',
        'followers_label': 'Dados JSON de Seguidores',
        
        # Placeholders
        'following_placeholder': '''Cole o conteúdo do seu following.json aqui...

Exemplo:
{
  "relationships_following": [
    {
      "string_list_data": [
        {
          "href": "...",
          "value": "usuario1",
          "timestamp": 1234567890
        }
      ]
    }
  ]
}''',
        
        'followers_placeholder': '''Cole o conteúdo do seu followers_1.json aqui...

Exemplo:
[
  {
    "string_list_data": [
      {
        "href": "...",
        "value": "seguidor1",
        "timestamp": 1234567890
      }
    ]
  }
]''',
        
        # Descriptions
        'following_description': 'Cole o conteúdo completo do seu arquivo "following.json"',
        'followers_description': 'Cole o conteúdo completo do seu arquivo "followers_1.json"',
        
        # Validation
        'validation_waiting': 'Validação JSON: Aguardando entrada',
        'validation_valid': 'Validação JSON: Formato JSON válido ✓',
        'validation_invalid': 'Validação JSON: Formato JSON inválido ✗',
        
        # Submit button
        'submit_button': 'Analisar Dados JSON',
        
        # Help sections
        'json_help': {
            'title': 'Ajuda com Formato JSON',
            'description': 'Certifique-se de que seus dados JSON sigam o formato correto de exportação do Instagram. O sistema validará sua entrada automaticamente.',
            'format_example': '''following.json: {"relationships_following": [...]}
followers_1.json: [{"string_list_data": [...]}]'''
        },
        
        'tutorial_help': {
            'title': 'Precisa de Ajuda para Obter Seus Dados?',
            'description': 'Nosso tutorial passo a passo irá guiá-lo através do download da sua exportação de dados do Instagram.',
            'button': 'Ver Tutorial'
        }
    },
    
    'fr': {
        # Meta data
        'title': 'Coller Données JSON - Analytics Instagram',
        
        # Header
        'header_title': 'Coller Données JSON',
        'header_description': 'Copiez et collez vos données JSON Instagram directement pour une analyse rapide',
        
        # Form labels
        'following_label': 'Données JSON d\'Abonnements',
        'followers_label': 'Données JSON d\'Abonnés',
        
        # Placeholders
        'following_placeholder': '''Collez le contenu de votre following.json ici...

Exemple:
{
  "relationships_following": [
    {
      "string_list_data": [
        {
          "href": "...",
          "value": "utilisateur1",
          "timestamp": 1234567890
        }
      ]
    }
  ]
}''',
        
        'followers_placeholder': '''Collez le contenu de votre followers_1.json ici...

Exemple:
[
  {
    "string_list_data": [
      {
        "href": "...",
        "value": "abonné1",
        "timestamp": 1234567890
      }
    ]
  }
]''',
        
        # Descriptions
        'following_description': 'Collez le contenu complet de votre fichier "following.json"',
        'followers_description': 'Collez le contenu complet de votre fichier "followers_1.json"',
        
        # Validation
        'validation_waiting': 'Validation JSON : En attente de saisie',
        'validation_valid': 'Validation JSON : Format JSON valide ✓',
        'validation_invalid': 'Validation JSON : Format JSON invalide ✗',
        
        # Submit button
        'submit_button': 'Analyser Données JSON',
        
        # Help sections
        'json_help': {
            'title': 'Aide Format JSON',
            'description': 'Assurez-vous que vos données JSON suivent le format d\'exportation Instagram correct. Le système validera automatiquement votre saisie.',
            'format_example': '''following.json: {"relationships_following": [...]}
followers_1.json: [{"string_list_data": [...]}]'''
        },
        
        'tutorial_help': {
            'title': 'Besoin d\'Aide pour Obtenir Vos Données ?',
            'description': 'Notre tutoriel étape par étape vous guidera à travers le téléchargement de votre exportation de données Instagram.',
            'button': 'Voir Tutoriel'
        }
    }
}
