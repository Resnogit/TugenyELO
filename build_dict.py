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
    match_id = 1
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
        )
        match_class_list.append(new_match)
        match_id += 1
    return match_class_list
