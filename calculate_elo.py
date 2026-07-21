from constants import MATCH_BASE_ELO

def calculate_elo(match_db):
    counted_matches = set()
    for game in match_db:
        match_id = game.get_id()
        winner = game.get_winner()
        looser = game.get_looser()
        match_counter = 1
        winner_wins = 1
        looser_wins = 0
        ## CHECK previous games
        for each in counted_matches:
            teams = (each.first_team, each.second_team)
            if winner in teams and looser in teams:
                match_counter += 1
                if winner == each.victorious_team:
                    winner_wins += 1
                else:
                    looser_wins += 1
        ##


        counted_matches.add(game)
        print(f"Parsing Match #{match_id}: Won: {winner} Lost: {looser} ({counter} matches between teams)")



def compare_elo(team1, team2):
    pass

def expected_elo(team1, team2):
    pass
