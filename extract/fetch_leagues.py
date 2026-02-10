import requests
from config.settings import API_FOOTBALL_BASE_URL, HEADERS

def fetch_leagues():
    url = f"{API_FOOTBALL_BASE_URL}/leagues"
    response = requests.get(url, headers=HEADERS)

    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = fetch_leagues()
    print(f"Total leagues returned: {len(data.get('response', []))}")
    print(data.get("response", [])[:2])  # preview
