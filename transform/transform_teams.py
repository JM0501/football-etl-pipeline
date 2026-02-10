from .utils import convert_numpy_to_python

def transform_teams(raw_teams):
    teams = []
    for item in raw_teams:
        team = {
            "team_id": item.get("team", {}).get("id"),
            "name": item.get("team", {}).get("name"),
            "country": item.get("team", {}).get("country"),
            "founded": item.get("team", {}).get("founded"),
            "venue_name": item.get("venue", {}).get("name"),
            "venue_capacity": item.get("venue", {}).get("capacity")
        }
        teams.append(convert_numpy_to_python(team))
    return teams

