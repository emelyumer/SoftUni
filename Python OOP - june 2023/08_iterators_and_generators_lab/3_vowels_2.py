class vowels:
    def __init__(self, symbols):
        self.symbols = symbols
        vowel = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U"]
        self.start_idx = -1
        self.end_idx = len(symbols) - 1
        self.current_idx = self.start_idx
        self.vowel_symbols = [v for v in self.symbols if v in vowel]

    def __iter__(self):
        return self.vowel_symbols


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)