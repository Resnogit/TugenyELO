from build_dict import build_match_db, build_teams_db
from classes import match, team

path_teams_json = "json/2025_teams.json"
path_matches_json = "json/2025_matches.json"


def calculate_elo(match_db, team_db):
    for match in match_db:
        team_1 = match.first_team
        team_2 = match.second_team
        winner = match.get_winner()
        for team in team_db:
            if team.name == team_1 or team.name == team_2:
                team.matches += 1
            if team.name == winner:
                team.wins += 1
    for team in team_db:
        winrate = team.get_winrate()
        print(
            f"{team.name}:{team.matches} matches; {team.wins} won. Winrate: {winrate}"
        )


def main():
    team_db = build_teams_db(path_teams_json)
    match_db = build_match_db(path_matches_json)
    calculate_elo(match_db, team_db)


main()
