class match:
    def __init__(self, first_team, second_team, victorious_team) -> None:
        self.__first_team = first_team
        self.__second_team = second_team
        self.__victorious_team = victorious_team

    def get_winner(self):
        return self.__victorious_team


class team:
    def __init__(self, id, name) -> None:
        self.__id = id
        self.name = name
        self.__elo = 1500

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.name
