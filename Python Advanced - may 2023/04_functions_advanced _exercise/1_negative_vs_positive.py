def sum_number(args):
    pos_list = list()
    neg_list = list()
    for el in args:
        if el > 0:
            pos_list.append(el)
        else:
            neg_list.append(el)
    if abs(sum(neg_list)) > sum(pos_list):
        return f"{sum(neg_list)}\n{sum(pos_list)}\nThe negatives are stronger than the positives"
    else:
        return f"{sum(neg_list)}\n{sum(pos_list)}\nThe positives are stronger than the negatives"


print(sum_number([int(x) for x in input().split()]))