def transform_fixtures(raw_fixtures):
    """
    Transform raw fixture data for MongoDB insertion.
    Args:
        raw_fixtures (list): Raw data from API-Football fetch_fixtures
    Returns:
        list: Transformed fixtures
    """
    transformed = []
    for item in raw_fixtures:
        fixture = item.get("fixture", {})
        league = item.get("league", {})
        teams = item.get("teams", {})
        score = item.get("score", {})

        transformed.append({
            "fixture_id": fixture.get("id"),
            "date": fixture.get("date"),
            "status": fixture.get("status", {}).get("short"),
            "league_id": league.get("id"),
            "home_team": teams.get("home", {}),
            "away_team": teams.get("away", {}),
            "score": score
        })
    return transformed

if __name__ == "__main__":
    from extract.fetch_fixtures import fetch_fixtures
    raw = fetch_fixtures(39, 2023)
    transformed = transform_fixtures(raw)
    print(transformed[:2])
