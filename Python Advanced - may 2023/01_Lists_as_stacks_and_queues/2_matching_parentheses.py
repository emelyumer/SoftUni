some_text = input()
open_parentheses_index = []
for index in range(len(some_text)):
    element = some_text[index]
    if element == "(":
        open_parentheses_index.append(index)
    elif element == ")":
        if len(open_parentheses_index) > 0:
            start_idx = open_parentheses_index.pop()
            end_idx = index + 1
            sep_parentheses = some_text[start_idx:end_idx]
            print(sep_parentheses)
