# def words_sorting(*words):
#     words_dict = {word: sum(map(ord, word)) for word in words}
#
#     if sum(words_dict.values()) % 2 == 0:
#         return "\n".join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: x[0])])
#
#     return "\n".join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: -x[1])])



def words_sorting(*args):
    sorted_words = dict()
    for word in args:
        sum_w = 0
        for let in word:
            sum_w += ord(let)
        sorted_words[word] = sum_w
    if sum(list(sorted_words.values())) % 2 == 0:
        return '\n'.join(f"{key} - {value}" for key, value in dict(sorted(sorted_words.items(), key=lambda x: x[0])).items())
    elif sum(list(sorted_words.values())) % 2 != 0:
        return '\n'.join(f"{key} - {value}" for key, value in dict(sorted(sorted_words.items(), key=lambda x: x[1], reverse=True)).items())


print(
 words_sorting(
 'escape',
 'charm',
 'mythology'
 ))
print(
 words_sorting(
 'escape',
 'charm',
 'eye'
 ))
print(
 words_sorting(
 'cacophony',
 'accolade'
 ))