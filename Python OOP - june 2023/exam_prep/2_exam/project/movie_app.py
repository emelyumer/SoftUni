from typing import List
from project.movie_specification.movie import Movie

from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        existing_user = [u for u in self.users_collection if u.username == username]

        if existing_user:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = [u for u in self.users_collection if u.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if movie.owner.username != username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        # Ines
        # if user.username != movie.owner.username:
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
            # if key == "year":
            #     movie.year = max(value, 1888)
            # elif key == "title" and value != "":
            #     movie.title = value
            # elif key == "age_restriction":
            #     if isinstance(movie, Fantasy):
            #         movie.age_restriction = max(value, 6)
            #     elif isinstance(movie, Action):
            #         movie.age_restriction = max(value, 12)
            #     elif isinstance(movie, Thriller):
            #         movie.age_restriction = max(value, 16)

        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda o: (-o.year, o.title))

        if not sorted_movies:
            return "No movies found."

        return "\n".join([m.details() for m in sorted_movies])

    def __str__(self):
        all_users = [u.username for u in self.users_collection]
        all_movies = [m.title for m in self.movies_collection]

        result = ''
        if not all_users:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join(all_users)}\n"
        if not all_movies:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join(all_movies)}"

        return result































