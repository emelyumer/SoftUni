some_text = input().split()
new_text = []
for index in range(len(some_text)):
    last_symbol = some_text.pop()
    new_text.append(last_symbol)
print(' '.join(new_text))
