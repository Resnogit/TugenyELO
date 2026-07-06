import json

from classes import match, team

path_teams_json = "json/2025_teams.json"


def json_to_dict(path):
    with open(path) as data:
        data_str = data.read()  # Reads path into a string
    dict_from_json = json.loads(data_str)  # creates dict object from json text
    return dict_from_json["teams"]


def teams_dict_to_class(dict):
    for team_dict in dict:
        new_team = team(team_dict["id"], team_dict["name"])


print(teams_dict_to_class(json_to_dict((path_teams_json))))
