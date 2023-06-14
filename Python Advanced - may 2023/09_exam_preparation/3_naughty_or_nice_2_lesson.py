def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids, naughty_kids = [], []
    result = []

    def place_kid():
        if len(kids) == 1:
            nice_kids.append(kids[0][1]) if type_of_kid == "Nice" else naughty_kids.append(kids[0][1])
            santa_list.remove(*kids)

    for kid_data in args:
        number, type_of_kid = kid_data.split("-")
        kids = [info for info in santa_list if info[0] == int(number)]
        place_kid()

    for name, type_of_kid in kwargs.items():
        kids = [info for info in santa_list if info[1] == name]
        place_kid()

    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")
    if santa_list:
        result.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

    return "\n".join(result)


print(naughty_or_nice_list(
 [
 (7, "Peter"),
 (1, "Lilly"),
 (2, "Peter"),
 (12, "Peter"),
 (3, "Simon"),
 ],
 "3-Nice",
 "5-Naughty",
 "2-Nice",
 "1-Nice",
 ))

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
