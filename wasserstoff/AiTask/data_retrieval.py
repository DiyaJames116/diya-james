import requests

WORDPRESS_API_URL = "https://public-api.wordpress.com/rest/v1.1/sites/diyajames.wordpress.com/posts"

def fetch_wordpress_content(api_url=WORDPRESS_API_URL):
    response = requests.get(api_url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Error decoding JSON response.")
            return None
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")
        return None


