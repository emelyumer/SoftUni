def reverse_text(text):
    last_idx = 0
    current_idx = len(text) - 1
    while current_idx >= last_idx:
        yield text[current_idx]
        current_idx -= 1


for char in reverse_text("step"):
    print(char, end='')