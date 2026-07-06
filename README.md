## Tugeny ELO Calculator

**currently in development**

This pyhton app is being designed to:
- Grab a list of teams from the Tugeny API (https://tugeny.org/api/).
- Grab all matches between given Teams from API.
- Calculate an ELO on Teams' comparative performance against each other.
- Export this ELO data to a .csv or other readable format.

Files:
- main.py:
  - Currently does nothing. Once parts are ready, the program will be called from here.
- classes.py:
  - Defines two relevant classes "match" and "team" that will hold the data gathered from the API to be worked with in calculating ELO.
- build_dict.py: 
  - contains functions for building iterable lists of match and team classes from the given json.
- calls.py: 
  - handles calling the tugeny API. Currently not in use, likely to be integrated into build_dict in the future.
