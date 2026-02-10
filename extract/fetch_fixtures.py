import requests
from config.settings import API_FOOTBALL_BASE_URL, HEADERS

def fetch_fixtures(league_id: int, season: int):
    """
    Fetch all fixtures for a given league and season.
    Args:
        league_id (int): League ID from API-Football
        season (int): Season year
    Returns:
        list: List of raw fixture data
    """
    url = f"{API_FOOTBALL_BASE_URL}/fixtures"
    params = {"league": league_id, "season": season}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json().get("response", [])

if __name__ == "__main__":
    league_id = 39  # Premier League
    season = 2023
    fixtures = fetch_fixtures(league_id, season)
    print(f"Total fixtures returned: {len(fixtures)}")
    print(fixtures[:2])  # preview first 2 fixtures
