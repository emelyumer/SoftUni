from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words_dict = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

while vowels and consonants:
    v_char = vowels.popleft()
    c_char = consonants.pop()
    for word in words_dict:
        if v_char in words_dict[word]:
            words_dict[word] = words_dict[word].replace(v_char, '')
        if c_char in words_dict[word]:
            words_dict[word] = words_dict[word].replace(c_char, '')
        if not words_dict[word]:
            print(f"Word found: {word}")
            break
    else:
        continue

    break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")









