from .utils import convert_numpy_to_python

def transform_fixtures(raw_fixtures):
    fixtures = []
    for item in raw_fixtures:
        fixture = {
            "fixture_id": item.get("fixture", {}).get("id"),
            "date": item.get("fixture", {}).get("date"),
            "home_team": item.get("teams", {}).get("home", {}).get("id"),
            "away_team": item.get("teams", {}).get("away", {}).get("id"),
            "league_id": item.get("league", {}).get("id"),
            "status": item.get("fixture", {}).get("status", {}).get("short")
        }
        fixtures.append(convert_numpy_to_python(fixture))
    return fixtures


