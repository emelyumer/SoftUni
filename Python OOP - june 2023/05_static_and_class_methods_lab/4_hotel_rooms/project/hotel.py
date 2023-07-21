from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        t_room = [r for r in self.rooms if r.number == room_number][0]
        res = t_room.take_room(people)
        if not res:
            self.guests += people

    def free_room(self, room_number):
        f_room = [r for r in self.rooms if r.number == room_number][0]
        guest_count = f_room.guests
        res = f_room.free_room()
        if not res:
            self.guests -= guest_count

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" + \
               f"Free rooms: {', '.join([f'{r.number}' for r in self.rooms if not r.is_taken])}\n" + \
               f"Taken rooms: {', '.join([f'{r.number}' for r in self.rooms if r.is_taken])}"




