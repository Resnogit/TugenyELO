from build_dict import build_match_db, build_opponents_set, build_teams_db, calculate_matches, clean_up_teams
from calculate_elo import calculate_elo
from generate_results import report_ranking

path_teams_json = "json/2025_teams.json"
path_matches_json = "json/2025_matches.json"


def main():
    team_db = build_teams_db(path_teams_json)
    match_db = build_match_db(path_matches_json)
    calculate_matches(match_db, team_db)
    team_db_clean = clean_up_teams(team_db)
    build_opponents_set(match_db, team_db_clean)
    calculate_elo(match_db, team_db_clean)
    report_ranking(team_db_clean)




main()
