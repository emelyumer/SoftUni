from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        try:
            playerr= [p for p in self.__players if p.name == player_name][0]
        except IndexError:
            return f"Player {player_name} not found"

        self.__players.remove(playerr)
        return playerr






