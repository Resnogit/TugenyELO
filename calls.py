import requests


def get_teams():
    # Define the API endpoint URL
    url = "https://tugeny.org/api/persistent/teams"
    # Make a GET request to the API endpoint using requests.get()
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        teams = response.json()
        return teams
    else:
        print("Error:", response.status_code)
        return None
