def transform_teams(raw_teams):
    """
    Transform raw team data for MongoDB insertion.
    Args:
        raw_teams (list): Raw data from API-Football fetch_teams
    Returns:
        list: Transformed teams
    """
    transformed = []
    for item in raw_teams:
        team = item.get("team", {})
        venue = item.get("venue", {})

        transformed.append({
            "team_id": team.get("id"),
            "name": team.get("name"),
            "logo": team.get("logo"),
            "venue_name": venue.get("name"),
            "venue_address": venue.get("address"),
            "venue_capacity": venue.get("capacity"),
            "venue_surface": venue.get("surface")
        })
    return transformed

if __name__ == "__main__":
    from extract.fetch_teams import fetch_teams
    raw = fetch_teams(39, 2023)  # Premier League example
    transformed = transform_teams(raw)
    print(transformed[:2])
