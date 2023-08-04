from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Player):
        added_players = []
        for p in players:
            if p not in self.players:
                self.players.append(p)
                added_players.append(p)
        return f"Successfully added: {', '.join([pl.name for pl in added_players])}"

    def add_supply(self, *supply):
        for s in supply:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = [p for p in self.players if p.name == player_name][0]
        except IndexError:
            return

        if sustenance_type not in ["Food", "Drink"]:
            return

        if sustenance_type == "Drink":
            try:
                drink = [d for d in self.supplies if d.__class__.__name__ == "Drink"][0]
            except IndexError:
                raise Exception("There are no drink supplies left!")

        if sustenance_type == "Food":
            try:
                food = [f for f in self.supplies if f.__class__.__name__ == "Food"][0]
            except IndexError:
                raise Exception("There are no food supplies left!")

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        for index in range(len(self.supplies)-1, -1, -1):
            supplies = self.supplies[index]
            if supplies.__class__.__name__ == sustenance_type:
                needed_supply = self.supplies.pop(index)
                player.stamina = min(needed_supply.energy + player.stamina, 100)
                return f"{player.name} sustained successfully with {needed_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        f_player = [p for p in self.players if p.name == first_player_name][0]
        s_player = [p for p in self.players if p.name == second_player_name][0]
        if f_player.stamina == 0 and s_player.stamina == 0:
            result = f"Player {f_player.name} does not have enough stamina.\n"
            result += f"Player {s_player.name} does not have enough stamina."
            return result

        if f_player.stamina == 0:
            return f"Player {f_player.name} does not have enough stamina."

        if s_player.stamina == 0:
            return f"Player {s_player.name} does not have enough stamina."

        if f_player.stamina > 0 and s_player.stamina > 0:
            if f_player.stamina > s_player.stamina:
                second_attacker = f_player
                first_attacker = s_player
            else:
                first_attacker = f_player
                second_attacker = s_player

            # first attack
            second_attacker.stamina -= first_attacker.stamina / 2
            if second_attacker.stamina <= 0:
                second_attacker.stamina = 0
                return f"Winner: {first_attacker.name}"

            # second attack
            first_attacker.stamina -= second_attacker.stamina / 2
            if first_attacker.stamina <= 0:
                return f"Winner: {second_attacker.name}"

            # we compair their stamina for winner
            if first_attacker.stamina > second_attacker.stamina:
                return f"Winner: {first_attacker.name}"
            else:
                return f"Winner: {second_attacker.name}"

    def next_day(self):
        for p in self.players:
            p.stamina = max(p.stamina - p.age * 2, 0)
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        return "\n".join(
            [str(p) for p in self.players]
            +
            [s.details() for s in self.supplies]
        )













