from constants import MATCH_BASE_ELO

def calculate_elo(match_db):
    counted_matches = set()
    for game in match_db:
        match_id = game.get_id()
        winner = game.get_winner()
        looser = game.get_looser()
        counter = 1
        for each in counted_matches:
            teams = (each.first_team, each.second_team)
            if winner in teams and looser in teams:
                counter+=1
        counted_matches.add(game)
        print(f"Parsing Match #{match_id}: Won: {winner} Lost: {looser} ({counter} matches between teams)")



def compare_elo(team1, team2):
    pass

def expected_elo(team1, team2):
    pass
