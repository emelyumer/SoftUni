class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_idx = self.count + 1
        self.end_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx -= 1
        if self.current_idx < 0:
            raise StopIteration

        return self.current_idx



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
 print(item, end=" ")