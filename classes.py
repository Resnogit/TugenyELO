class match:
    def __init__(
        self,
        first_team,
        first_team_id,
        second_team,
        second_team_id,
        victorious_team,
        victorious_team_id,
    ) -> None:
        self.first_team = first_team
        self.__first_team_id = first_team_id
        self.second_team = second_team
        self.__second_team_id = second_team_id
        self.victorious_team = victorious_team
        self.__victorious_team_id = victorious_team_id

    def get_winner(self):
        return self.victorious_team


class team:
    def __init__(self, id, name) -> None:
        self.__id = id
        self.name = name
        self.elo = 1500
        self.matches = 0
        self.wins = 0
        self.__winrate = 0.00

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.name

    def get_winrate(self):
        try:
            self.__winrate = (self.wins / self.matches) * 100
        except ZeroDivisionError:
            print("No Matches found. Can not calculate Winrate")
        return f"{self.__winrate:.2f}%"
