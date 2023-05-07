number = tuple(map(float, input().split()))
counted_num = {x:number.count(x) for x in number}
for k,v in counted_num.items():
    print(f"{k} - {v} times")
