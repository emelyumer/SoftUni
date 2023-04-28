# first way
# some_text = input()
# reversed_text = some_text[::-1]
# print(reversed_text)

# second way
new_text = []
some_text = list(input())
for index in range(len(some_text)):
    symbol = some_text.pop()
    new_text.append(symbol)
print(''.join(new_text))
