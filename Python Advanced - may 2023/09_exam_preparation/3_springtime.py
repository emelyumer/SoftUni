def start_spring(**kwargs):
    sorting_dict = dict()
    for key, value in kwargs.items():
        if value not in sorting_dict:
            sorting_dict[value] = []
        sorting_dict[value].append(key)

    sorted_dict = sorted(sorting_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for k, v in sorted_dict:
        v_sorted = sorted(v)
        result += f"{k}:\n"
        for vv in v_sorted:
            result += f"-{vv}\n"

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))