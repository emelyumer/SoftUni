from project.player import Player
from typing import List
class Guild:
    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild." #слагаме player.name(името) player а е инстанцията(обекта)
        if player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player) # не слагаме player_name(само името) а player, защото това е инстанцията(обекта)
        player.guild = Player.DEFAULT_GUILD
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join([p.player_info() for p in self.players])
        return f"Guild: {self.name}\n" + \
               f"{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())