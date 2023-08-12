from project.movie_specification.movie import Movie
from project.user import User


class Thriller(Movie):

    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, " \
               f"Year:{self.year}, Age restriction:{self.age_restriction}," \
               f" Likes:{self.likes}, Owned by:{self.owner.username}"


# u = User("test", 59)
# f = Thriller("ASD", 2000, u, 16)
# print(f.age_restriction)
