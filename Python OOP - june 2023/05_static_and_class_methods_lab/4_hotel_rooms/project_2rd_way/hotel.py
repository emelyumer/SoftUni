from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self):
        return sum([g.guests for g in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        t_room = [r for r in self.rooms if r.number == room_number][0]
        t_room.take_room(people)


    def free_room(self, room_number):
        f_room = [r for r in self.rooms if r.number == room_number][0]
        f_room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" + \
               f"Free rooms: {', '.join([f'{r.number}' for r in self.rooms if not r.is_taken])}\n" + \
               f"Taken rooms: {', '.join([f'{r.number}' for r in self.rooms if r.is_taken])}"




