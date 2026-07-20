from classes import match, team

def calculate_elo(match_db):
    for game in match_db:
        match_id = game.get_id()
        winner = game.get_winner()
        looser = game.get_looser()
        print(f"Parsing Match #{match_id}: Won: {winner} Lost {looser}")


def compare_elo(team1, team2):
    pass

def expected_elo(team1, team2):
    pass
