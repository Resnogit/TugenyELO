from build_dict import build_match_db, build_teams_db
from classes import match, team

path_teams_json = "json/2025_teams.json"
path_matches_json = "json/2025_matches.json"


def calculate_matches(match_db, team_db):
    for match in match_db:  # Checks if teams have participated in matches and increments their values accordingly
        match_id = match.get_id()
        team_1 = match.first_team
        team_2 = match.second_team
        winner = match.get_winner()
        # print(f"Parsing Match #{match_id}: {team_1} // {team_2}")
        for team in team_db:
            if team.name == team_1 or team.name == team_2:
                team.matches += 1
            if team.name == winner:
                team.wins += 1
    print(f"{match_id} matches found!")
    team_db_clean = []
    counter = 0
    print("Cleaning up teams...")
    for team in team_db:  # remove all teams with 0 matches from the db
        if team.matches <= 0:
            counter += 1
        else:
            team.get_winrate()  # Sets winrate for all teams with more than 0 matches
            team_db_clean.append(team)
    print(f"Removed {counter} teams with 0 recorded matches!")
    return team_db_clean


def report_winrates(team_db):
    for team in team_db:
        winrate = team.get_winrate()
        print(f"{team.name}: {team.wins}/{team.matches} matches won! ({winrate})")


def main():
    team_db = build_teams_db(path_teams_json)
    match_db = build_match_db(path_matches_json)
    calculate_matches(match_db, team_db)


main()
