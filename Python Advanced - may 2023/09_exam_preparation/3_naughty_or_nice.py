from collections import deque
def naughty_or_nice_list(kids, *args, **kwargs):
    kids = deque(kids)
    CHECK = [k[0] for k in kids]
    CHECK2 = [k[1] for k in kids]
    final = {"Nice": [], "Naughty": [], "Not found": []}
    rating = {}
    counter = len(kids)
    idx = 0
    for r in args:
        r = r.split("-")
        rating[r[0]] = r[1]

    while idx < counter:
        idx += 1
        rk = kids.popleft()
        check_rate = rk[0]
        check_count = CHECK.count(check_rate)
        if check_count > 1:
            kids.append(rk)
            continue
        number = str(rk[0])
        if number in list(rating.keys()):
            final[rating[number]].append(rk[1])
        else:
            kids.append(rk)



    if kwargs:
        while kids:
            nk = kids.popleft()
            name = nk[1]
            name_counter = CHECK2.count(name)
            if name_counter > 1:
                final["Not found"].append(name)
                continue

            if name in list(kwargs.keys()):
                final[kwargs[name]].append(name)
            else:
                final["Not found"].append(name)
    else:
        final["Not found"].extend([k[1] for k in kids])

    return '\n'.join([f"{key}: {', '.join(value)}" for key, value in final.items() if value])



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