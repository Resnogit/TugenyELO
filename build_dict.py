import json

from classes import match, team


def build_teams_db(path):
    team_class_list = []  # New list container for resulting list.
    with open(path) as data:
        data_str = data.read()  # Reads path into a string
    dict_from_json = json.loads(data_str)  # creates dict object from json text
    for team_dict in dict_from_json[
        "teams"
    ]:  # iterates over the new dict, only moving selected attributes to resulting teams list
        new_team = team(team_dict["id"], team_dict["name"])
        team_class_list.append(new_team)
    return team_class_list


def build_match_db(path):
    match_class_list = []  # Empty list for result
    match_id = 1  # Starting MatchID
    with open(path) as data:
        data_str = data.read()  # Reads path into a string
    dict_from_json = json.loads(data_str)  # creates dict object from json text
    for match_dict in dict_from_json:
        new_match = match(
            match_id,
            match_dict["first_team"],
            match_dict["first_team_id"],
            match_dict["second_team"],
            match_dict["second_team_id"],
            match_dict["victorious_team"],
            match_dict["victorious_team_id"],
            match_dict["timestamp"]
        )
        match_class_list.append(
            new_match
        )  # Adds a match object according to the above format to a list.
        match_id += 1  # Increments Match ID.
    return match_class_list


def calculate_matches(match_db, team_db):
    for match in match_db:  # Checks if teams have participated in matches and increments their values accordingly. This is necessary BEFORE cleanup can happen!
        match_id = match.get_id()
        for team in team_db:
            if team.name == match.first_team or team.name == match.second_team:
                team.matches += 1
            if team.name == match.victorious_team:
                team.wins += 1
    print(f"Match data updated: {match_id} matches found!")


def clean_up_teams(team_db):
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

def build_opponents_set(match_db, team_db):
    for team in team_db:
        team.get_opponents(match_db)
