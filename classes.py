from constants import BASE_ELO_VALUE

class match:
    def __init__(
        self,
        match_id,
        first_team,
        first_team_id,
        second_team,
        second_team_id,
        victorious_team,
        victorious_team_id,
        timestamp
    ) -> None:
        self.first_team = first_team
        self.__first_team_id = first_team_id
        self.second_team = second_team
        self.__second_team_id = second_team_id
        self.teams = (first_team, second_team)
        self.victorious_team = victorious_team
        self.__victorious_team_id = victorious_team_id
        self.id = match_id
        self.timestamp = timestamp

    def get_looser(self):
        return self.first_team if self.second_team == self.victorious_team else self.second_team

    def get_winner(self):
        return self.victorious_team

    def get_winner_obj(self, team_db:list) -> object:
        for team in team_db:
            if self.get_winner() == team.name:
                return team

    def get_looser_obj(self, team_db:list) -> object:
        for team in team_db:
            if self.get_looser() == team.name:
                return team

    def get_id(self):
        return self.id

    def get_participants_obj(self, team_db: list): #Rewrite into callable attributes for each team in the match
        for team in team_db:
            if team.name == self.first_team:
                participant1 = team
            if team.name == self.second_team:
                participant2 = team
        return participant1, participant2


class team:
    def __init__(self, id: int, name: str) -> None:
        self.__id = id
        self.name = name
        self.elo = 0
        self.matches = 0
        self.wins = 0
        self.__winrate = 0.00
        self.opponents = set()
        self.match_gp = 0
        self.prev_rank = 1
        self.rank = None
        self.matchups = set()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.name

    def get_winrate(self):
        try:
            self.__winrate = (self.wins / self.matches) * 100
        except ZeroDivisionError:
            print(f"No Matches found for {self.name}. Can not calculate Winrate")
        return f"{self.__winrate:.2f}%"

    def get_opponents(self, matches:list):
        for match in matches:
            if self.name in match.teams:
                if match.teams[0] == self.name:
                    opponent = match.teams[1]
                else:
                    opponent = match.teams[0]
                self.opponents.add(opponent)
        return self.opponents

class matchup: #NEEDS "find_matchups" somewhere to build this. ?Build_dict=?
    def __init__(self,team1:str, team2:str ,match_db:list) -> None:
        self.team1 = team1
        self.team2 = team2
        self.teams = (team1, team2)
        self.wins_team1 = 0
        self.wins_team2 = 0
        self.draws = 0
        self.calculate_wins_draws(match_db)
        self.total_matches = self.wins_team1 + self.wins_team2 + self.draws
        self.__matchcoeff = self.wins_team1 - self.wins_team2

    def calculate_wins_draws(self, match_db):
        for match in match_db:
            if self.team1 in match.teams and self.team2 in match.teams:
                if match.victorious_team == None:
                    self.draws +=1
                if match.victorious_team == self.team1:
                    self.wins_team1 +=1
                if match.victorious_team == self.team2:
                    self.wins_team2 +=1
