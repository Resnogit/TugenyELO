import json

from classes import match, team

path_teams_json = "json/2025_teams.json"
path_matches_json = "json/2025_matches.json"


def teams_json_to_dict(path):
    with open(path) as data:
        data_str = data.read()  # Reads path into a string
    dict_from_json = json.loads(data_str)  # creates dict object from json text
    return dict_from_json["teams"]


def teams_dict_to_class(dict):
    team_class_list = []  # New list container
    for team_dict in dict:
        new_team = team(
            team_dict["id"], team_dict["name"]
        )  # Iterates over Teams.json list g
        team_class_list.append(new_team)
    return team_class_list


def match_json_to_dict(path):
    with open(path) as data:
        data_str = data.read()  # Reads path into a string
    dict_from_json = json.loads(data_str)  # creates dict object from json text
    return dict_from_json


def match_dict_to_class(dict):
    match_class_list = []
    for match_dict in dict:
        new_match = match(
            match_dict["first_team"],
            match_dict["first_team_id"],
            match_dict["second_team"],
            match_dict["second_team_id"],
            match_dict["victorious_team"],
            match_dict["victorious_team_id"],
        )
        match_class_list.append(new_match)
    return match_class_list


# list_of_teams = teams_dict_to_class(teams_json_to_dict((path_teams_json)))
# list_of_matches = match_dict_to_class(match_json_to_dict(path_matches_json))
