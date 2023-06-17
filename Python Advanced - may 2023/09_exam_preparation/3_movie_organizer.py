# https://judge.softuni.org/Contests/Practice/Index/3893#2

def movie_organizer(*args):
    sorting_dict = dict()
    for movie in args:
        if movie[1] not in sorting_dict.keys():
            sorting_dict[movie[1]] = []
        sorting_dict[movie[1]].append(movie[0])

    sorted_dict = dict(sorted(sorting_dict.items(), key=lambda item: (-len(item[1]), item[0])))

    result = ""
    for key, value in sorted_dict.items():
        value = sorted(value)
        result += f"{key} - {len(value)}\n"
        for v in value:
            result += f"* {v}\n"

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

