from classes import match, team

def calculate_elo(match_db):
    for game in match_db:
        match_id = game.get_id()
        team_1 = game.first_team
        team_2 = game.second_team
        winner = game.get_winner()
        print(f"Parsing Match #{match_id}: {team_1} // {team_2}")



def compare_elo(team1, team2):
    pass

def expected_elo(team1, team2):
    pass
