class vowels:
    def __init__(self, symbols):
        self.symbols = symbols
        self.start_idx = 0
        self.end_idx = len(symbols) - 1
        self.current_idx = self.start_idx

    def __iter__(self):
        return self

    def __next__(self):
        vowel = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U"]
        if self.current_idx > self.end_idx:
            raise StopIteration()
        temp_idx = self.current_idx
        self.current_idx += 1
        if self.symbols[temp_idx] in vowel:
            return self.symbols[temp_idx]
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
