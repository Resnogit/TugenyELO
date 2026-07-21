from constants import MATCH_BASE_ELO

def calculate_elo(match_db, team_db):
    counted_matches = set()
    for game in match_db:
        match_id = game.get_id()
        winner = game.get_winner_obj(team_db)
        looser = game.get_looser_obj(team_db)
        if check_if_not_draw(game):
            previous_check = check_previous_matches(counted_matches, winner, looser)
            match_counter = previous_check[0]
            winner_wins = previous_check[1]
            looser_wins = previous_check[2]
            calculate_points(winner, winner_wins, looser, looser_wins, match_counter)
            counted_matches.add(game)
            print(f"Parsing Match #{match_id}: Won: {winner.name} ({winner.elo}) Lost: {looser.name} ({looser.elo})")
        else:
            counted_matches.add(game)
            print(f"Parsing Match #{match_id}: DRAW! {game.first_team} // {game.second_team}")
        ##
        #calculate_points(winner, winner_wins, looser, looser_wins, match_counter)





def check_if_not_draw(match):
    if match.victorious_team != None:
        return True

def check_previous_matches(counted_matches, winner, looser):
    match_counter = 1
    winner_wins = 1
    looser_wins = 0
    ## CHECK previous games
    for each in counted_matches:
        teams = (each.first_team, each.second_team)
        if winner.name in teams and looser.name in teams:
            match_counter += 1
            if winner.name == each.victorious_team:
                winner_wins += 1
            else:
                looser_wins += 1
    return match_counter, winner_wins, looser_wins

def calculate_points(winner, winner_wins, looser, looser_wins, match_counter):
    points_winner = looser_wins/(winner_wins + looser_wins) * winner.elo
    if match_counter == 1:
        winner.elo += MATCH_BASE_ELO + points_winner
        looser.elo += MATCH_BASE_ELO
    else:
        winner.elo += points_winner
