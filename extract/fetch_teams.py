import requests
from config.settings import API_FOOTBALL_BASE_URL, HEADERS

def fetch_teams(league_id: int, season: int):
    """
    Fetch all teams for a given league and season.
    Args:
        league_id (int): League ID from API-Football
        season (int): Season year (e.g., 2024)
    Returns:
        list: List of raw team data
    """
    url = f"{API_FOOTBALL_BASE_URL}/teams"
    params = {"league": league_id, "season": season}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json().get("response", [])
"""
if __name__ == "__main__":
    league_id = 39  # Premier League
    season = 2023
    teams = fetch_teams(league_id, season)
    print(f"Total teams returned: {len(teams)}")
    print(teams[:2])  # preview first 2 teams
"""