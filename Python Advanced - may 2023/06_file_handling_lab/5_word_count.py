import os
import re
from collections import defaultdict


def read_content(filepath):
    try:
        with open (filepath, "r") as file:
            return file.read()

    except FileNotFoundError:
        print("File does not exit, program is ending...")
        exit(0)



root_dir = os.path.dirname(os.path.abspath(__file__))
words_file_name = "words.txt"
words_file_path = os.path.join(root_dir, words_file_name)
input_file_name = "input.txt"
input_file_path = os.path.join(root_dir, input_file_name)

words = read_content(words_file_path).lower().split()
text_content = read_content(input_file_path).lower()
text_content = re.sub(r"[^\w+\s]", "", text_content)    # махаме всички точки, запетаи и дучи значи и остава само тект
text_content_lines = text_content.split("\n")    # изчиства \n и събира всеки нов ред в лист
words_count = defaultdict(lambda: 0)

for word in words:
    for text_line in text_content_lines:
        if word in text_line:
            words_count[word] += 1


print(words)
print(text_content)
with open("output.txt", "w") as file:
    for key, value in sorted(words_count.items(), key=lambda x: -x[1]):
        file.write(f"{key} - {value}\n")
