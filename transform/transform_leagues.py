
def transform_leagues(raw_leagues):
    """
    Transform raw league data for MongoDB insertion.
    Args:
        raw_leagues (list): Raw data from API-Football fetch_leagues
    Returns:
        list: Transformed leagues
    """
    transformed = []
    for item in raw_leagues:
        league = item.get("league", {})
        country = item.get("country", {})
        seasons = item.get("seasons", [])

        transformed.append({
            "league_id": league.get("id"),
            "name": league.get("name"),
            "type": league.get("type"),
            "logo": league.get("logo"),
            "country_name": country.get("name"),
            "country_code": country.get("code"),
            "current_season": next((s for s in seasons if s.get("current")), None),
            "all_seasons": seasons
        })
    return transformed

if __name__ == "__main__":
    from extract.fetch_leagues import fetch_leagues
    raw = fetch_leagues()
    transformed = transform_leagues(raw)
    print(transformed[:2])
