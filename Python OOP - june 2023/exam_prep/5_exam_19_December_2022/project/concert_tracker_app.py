from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    GENRE_NEEDED_SKILLS = {
        "Metal": {
            "Guitarist": "play metal",
            "Drummer": "play the drums with drumsticks",
            "Singer": "sing low pitch notes"
        },
        "Rock": {
            "Guitarist": "play rock",
            "Drummer": "play the drums with drumsticks",
            "Singer": "sing high pitch notes"
        },
        "Jazz": {
            "Guitarist": "play jazz",
            "Drummer": "play the drums with drum brushes",
            "Singer": ["sing high pitch notes", "sing low pitch notes"]
        }
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        musician = [m for m in self.musicians if m.name == name]
        if musician:
            raise Exception(f"{name} is already a musician!")

        musician = ConcertTrackerApp.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = [b for b in self.bands if b.name == name]
        if band:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]
        if concert:
            raise Exception(f"{place} is already registered for {concert[0].genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{concert.genre} concert in {concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band[0].members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = [m for m in band[0].members if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band[0].members.remove(musician[0])
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = [c for c in self.concerts if c.place == concert_place][0]
        band = [b for b in self.bands if b.name == band_name][0]

        singers = [m for m in band.members if isinstance(m, Singer)]
        if not singers:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")
        drummers = [m for m in band.members if isinstance(m, Drummer)]
        if not drummers:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")
        guitarists = [m for m in band.members if isinstance(m, Guitarist)]
        if not guitarists:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        for drummer in drummers:
            if concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif concert.genre == "Jazz":
                if "play the drums with drum brushes" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        for singer in singers:
            if concert.genre == "Rock":
                if "sing high pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif concert.genre == "Metal":
                if "sing low pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif concert.genre == "Jazz":
                if "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        for guitarist in guitarists:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif concert.genre == "Metal":
                if "play metal" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
            elif concert.genre == "Jazz":
                if "play jazz" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
