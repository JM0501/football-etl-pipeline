import requests
from config.settings import API_FOOTBALL_BASE_URL, HEADERS

def fetch_leagues():
    """
    Fetch all leagues from API-Football
    Returns:
        list: List of raw league data
    """
    url = f"{API_FOOTBALL_BASE_URL}/leagues"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("response", [])

if __name__ == "__main__":
    data = fetch_leagues()
    print(f"Total leagues returned: {len(data)}")
    print(data[:2])  # preview first 2 leagues
