from constants import BASE_ELO_VALUE, MATCH_BASE_ELO, POSITIONAL_ELO_MAX


def check_if_not_draw(match) -> bool:
    if match.victorious_team != None:
        return True
    return False

def check_previous_matches(counted_matches, team1, team2) -> tuple[int, int, int, int]:
    match_counter = 1
    team1_wins = 0
    team2_wins = 0
    draws = 0
    ## CHECK previous games
    for each in counted_matches:
        teams = (each.first_team, each.second_team)
        if team1.name in teams and team2.name in teams:
            match_counter += 1
            if each.victorious_team == None:
                draws += 1
            if team1.name == each.victorious_team:
                team1_wins += 1
            else:
                team2_wins += 1
    return match_counter, team1_wins, team2_wins, draws

def calculate_points(winner, winner_wins, looser, looser_wins, draws, match_counter) -> tuple[int, int]:
    points_winner = winner_wins/(winner_wins + looser_wins + draws) * looser.elo
    points_looser = looser_wins/(winner_wins + looser_wins + draws) * winner.elo
    winner_point_gain = points_winner
    looser_point_gain = points_looser
    if match_counter == 1:
        winner.elo += MATCH_BASE_ELO + points_winner
        looser.elo += MATCH_BASE_ELO + points_looser
        winner_point_gain += MATCH_BASE_ELO
        looser_point_gain += MATCH_BASE_ELO
    else:
        winner.elo += points_winner
        looser.elo += points_looser
    return winner_point_gain, looser_point_gain

def calculate_points_draw(team1, team2, match_counter):
    point_gain = 0
    if match_counter == 1:
        team1.elo += MATCH_BASE_ELO
        team2.elo += MATCH_BASE_ELO
        point_gain += MATCH_BASE_ELO
    return point_gain



def calculate_elo(match_db, team_db):
    counted_matches = set()
    print("Starting match parse for ELO calculation.")
    for game in match_db:
        match_id = game.get_id()
        winner = game.get_winner_obj(team_db)
        looser = game.get_looser_obj(team_db)
        if check_if_not_draw(game):
            match_counter, winner_wins, looser_wins, draws = check_previous_matches(counted_matches, winner, looser)
            if winner_wins + looser_wins + draws == 0:
                winner_wins = 1
            winner_point_gain, looser_point_gain = calculate_points(winner, winner_wins, looser, looser_wins, draws, match_counter)
            counted_matches.add(game)
            # print(f"Parsing Match #{match_id}: Won: {winner.name} gained {winner_point_gain:.2f} pts ({winner.elo:.2f}) Lost: {looser.name} gained {looser_point_gain:.2f} pts ({looser.elo:.2f}) ")
        else:
            team1, team2 = game.get_participants_obj(team_db)
            match_counter, *_ = check_previous_matches(counted_matches, team1, team2)
            point_gain = calculate_points_draw(team1, team2, match_counter)
            counted_matches.add(game)
            # print(f"Parsing Match #{match_id}: DRAW! {game.first_team} // {game.second_team} {point_gain} pts gained.")
    print(f"Parsed {len(counted_matches)} Matches!")
