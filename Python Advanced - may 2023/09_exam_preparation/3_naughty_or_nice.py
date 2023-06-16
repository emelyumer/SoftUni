# https://judge.softuni.org/Contests/Practice/Index/3306#2

completed_list = {"Nice": [], "Naughty": [], "Not found": []}

def naughty_or_nice_list(kids_list, *args, **kwargs):

    for sorting in args:
        number, rate = sorting.split("-")
        matched_kids = []
        for kid in kids_list:
            if kid[0] == int(number):
                matched_kids.append(kid)
        if len(matched_kids) == 1:
            completed_list[rate].append(matched_kids[0][1])
            kids_list.remove(matched_kids[0])
        matched_kids.clear()

    for name, types in kwargs.items():
        matched_kids = []
        for kid in kids_list:
            if kid[1] == name:
                matched_kids.append(kid)
        if len(matched_kids) == 1:
            completed_list[types].append(matched_kids[0][1])
            kids_list.remove(matched_kids[0])
        matched_kids.clear()

    for kid in kids_list:
        completed_list["Not found"].append(kid[1])

    return '\n'.join([f"{key}: {', '.join(value)}" for key, value in completed_list.items() if value])


# print(naughty_or_nice_list(
#  [
#  (7, "Peter"),
#  (1, "Lilly"),
#  (2, "Peter"),
#  (12, "Peter"),
#  (3, "Simon"),
#  ],
#  "3-Nice",
#  "5-Naughty",
#  "2-Nice",
#  "1-Nice",
#  ))

print(naughty_or_nice_list(
 [
 (6, "John"),
 (4, "Karen"),
 (2, "Tim"),
 (1, "Merry"),
 (6, "Frank"),
 ],
 "6-Nice",
 "5-Naughty",
 "4-Nice",
 "3-Naughty",
 "2-Nice",
 "1-Naughty",
 Frank="Nice",
 Merry="Nice",
 John="Naughty",
))