class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list = []   # Ines List[Movie]
        self.movies_owned: list = []   # Ines List[Movie]

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\nLiked movies:\n"

        if not self.movies_liked:
            result += "No movies liked.\n"
        else:
            result += "\n".join([m.details() for m in self.movies_liked]) + "\n"

        if not self.movies_owned:
            result += "No movies owned."

        else:
            result += "\n".join([m.details() for m in self.movies_owned])

        return result
        