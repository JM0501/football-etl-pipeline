from .utils import convert_numpy_to_python

def transform_leagues(raw_leagues):
    leagues = []
    for item in raw_leagues:
        league = {
            "league_id": item.get("league", {}).get("id"),
            "name": item.get("league", {}).get("name"),
            "type": item.get("league", {}).get("type"),
            "country": item.get("country", {}).get("name"),
            "season": max([s.get("year") for s in item.get("seasons", [])]) if item.get("seasons") else None
        }
        leagues.append(convert_numpy_to_python(league))
    return leagues

