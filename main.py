from build_dict import build_match_db, build_teams_db, calculate_matches, clean_up_teams, write_db_to_file
from calculate_elo import calculate_elo
#Test Comment
path_teams_json = "json/2025_teams.json"
path_matches_json = "json/2025_matches.json"


def update_db(match_db, team_db):
    calculate_matches(match_db, team_db)
    clean_up_teams(team_db)


def report_winrates(team_db):
    for team in team_db:
        winrate = team.get_winrate()
        print(f"{team.name}: {team.wins}/{team.matches} matches won! ({winrate})")


def main():
    team_db = build_teams_db(path_teams_json)
    match_db = build_match_db(path_matches_json)
    update_db(match_db, team_db)
    calculate_elo(match_db)


main()
