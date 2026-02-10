from extract.fetch_leagues import fetch_leagues
from extract.fetch_teams import fetch_teams
from extract.fetch_fixtures import fetch_fixtures

from transform.transform_leagues import transform_leagues
from transform.transform_teams import transform_teams
from transform.transform_fixtures import transform_fixtures

from load.load_mongo import upsert_documents

# Config
LEAGUE_IDS = [39, 140]  # Example: Premier League, La Liga
SEASON = 2024

def main():
    print("🔹 Starting ETL pipeline...\n")

    # --- LEAGUES ---
    raw_leagues = fetch_leagues()
    print(f"Fetched {len(raw_leagues)} leagues from API.")
    leagues_data = transform_leagues(raw_leagues)
    print(f"Transformed {len(leagues_data)} leagues.")
    upserted_count = upsert_documents("leagues", leagues_data, key="league_id")
    print(f"Upserted {upserted_count} leagues into MongoDB.\n")

    # --- TEAMS ---
    for league_id in LEAGUE_IDS:
        raw_teams = fetch_teams(league_id, SEASON)
        print(f"Fetched {len(raw_teams)} teams for league {league_id}.")
        teams_data = transform_teams(raw_teams)
        print(f"Transformed {len(teams_data)} teams for league {league_id}.")
        upserted_count = upsert_documents("teams", teams_data, key="team_id")
        print(f"Upserted {upserted_count} teams into MongoDB.\n")

    # --- FIXTURES ---
    for league_id in LEAGUE_IDS:
        raw_fixtures = fetch_fixtures(league_id, SEASON)
        print(f"Fetched {len(raw_fixtures)} fixtures for league {league_id}.")
        fixtures_data = transform_fixtures(raw_fixtures)
        print(f"Transformed {len(fixtures_data)} fixtures for league {league_id}.")
        upserted_count = upsert_documents("fixtures", fixtures_data, key="fixture_id")
        print(f"Upserted {upserted_count} fixtures into MongoDB.\n")

    print("✅ ETL pipeline completed successfully!")


if __name__ == "__main__":
    main()
