from collections import deque
raw_colors = deque(input().split())
all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}
founded_colors = list()

while raw_colors:
    first_el = raw_colors.popleft()
    second_el = raw_colors.pop() if raw_colors else ""
    for check in (first_el + second_el, second_el + first_el):
        if check in all_colors:
            founded_colors.append(check)
            break
    else:
        # raw_colors.append(first_el[:-1] if None else)
        for unmatched_word in (first_el[:-1], second_el[:-1]):
            if unmatched_word:
                raw_colors.insert(len(raw_colors) // 2, unmatched_word)

for color in set(req_colors.keys()).intersection(founded_colors):
    if not req_colors[color].issubset(founded_colors):
        founded_colors.remove(color)

print(founded_colors)

