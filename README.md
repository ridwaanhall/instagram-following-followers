# Instagram Analytics

This project provides a Python script to analyze Instagram followers and following data. The script calculates various analytics such as the count of followers, following, mutual followers, and lists of users who don't follow back or are not followed back.

## Features

- Count of users you are following
- Count of users following you
- Count of mutual followers
- Count of users you follow but who don't follow you back
- Count of users who follow you but you don't follow back
- List of users you follow but who don't follow you back
- List of users who follow you but you don't follow back
- List of mutual followers

## Requirements

- Python 3.x

## Tutorial to Get JSON Data of Following and Followers

1. Go to your Instagram profile.
2. Click the top-right icon with three horizontal lines.
3. Click "Account Center".
4. In account settings, select "Your Information and Permissions".
5. Click "Download Your Information".
6. Click "Download or Transfer Information".
7. Select your account.
8. Select "Some of your information".
9. In the "Connections" section, select "Followers and Following".
10. Download to your device.
11. Set the date range to "All time" and format to "JSON".
12. Click the "Create Files" button.
13. After a few minutes, navigate to "Download Your Information".
14. After downloading, extract the files and copy the `following.json` and `followers_1.json` files to the same folder as `instagram_analytics.py`. Ensure the JSON files match the format used in the script.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/ridwaanhall/instagram-following-followers.git
    cd instagram-following-followers
    ```

2. Ensure you have the required JSON files (`following.json` and `followers_1.json`) in the project directory.

## Usage

1. Run the script:

    ```sh
    python instagram_analytics.py
    ```

2. The script will print the analytics to the console.

## Example JSON Files

### following.json

```json
{
  "relationships_following": [
    {
      "title": "",
      "media_list_data": [],
      "string_list_data": [
        {
          "href": "https://www.instagram.com/jhon.doe",
          "value": "jhon.doe",
          "timestamp": 17XXX
        }
      ]
    }
  ]
}
```

### followers_1.json

```json
[
  {
    "title": "",
    "media_list_data": [],
    "string_list_data": [
      {
        "href": "https://www.instagram.com/jhon.doe",
        "value": "jhon.doe",
        "timestamp": 17XXX
      }
    ]
  }
]
```

## License

This project is licensed under the [MIT License](LICENSE).
