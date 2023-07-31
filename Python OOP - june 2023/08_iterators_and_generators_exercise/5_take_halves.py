def solution():
    def integers():
        int_num = 1
        while True:
            yield int_num
            int_num += 1


    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq): # seq e  halves() от ред 22 се извиква така
        return [next(seq) for _ in range(n)]


    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))