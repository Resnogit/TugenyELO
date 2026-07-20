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
        self.victorious_team = victorious_team
        self.__victorious_team_id = victorious_team_id
        self.id = match_id
        self.timestamp = timestamp


    def get_winner(self):
        return self.victorious_team

    def get_id(self):
        return self.id


class team:
    def __init__(self, id, name) -> None:
        self.__id = id
        self.name = name
        self.elo = 1500
        self.matches = 0
        self.wins = 0
        self.__winrate = 0.00
        self.__opponents = {}

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

    def get_opponents(self, matches):
        for match in matches:
            teams = (match.first_team, match.second_team)
            if self.name in teams:
                if teams[0] == self.name:
                    opponent = teams[1]
                else:
                    opponent = teams[0]
                if opponent in self.__opponents:
                    self.__opponents[opponent] += 1
                else:
                    self.__opponents[opponent] = 1
        return self.__opponents
