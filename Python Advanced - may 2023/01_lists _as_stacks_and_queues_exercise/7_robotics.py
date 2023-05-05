from datetime import datetime, timedelta
from collections import deque

robots = {r.split("-")[0]:[int(r.split("-")[1]), 0] for r in input().split(";")}
# print(robots)
factory_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()
product = input()
while product != "End":
    products.append(product)
    product = input()
# print(products)
free_robots = []
while products:
    free_robots.clear()
    factory_time += timedelta(0, 1)
    assem_product = products.popleft()
    free_robots = list()
    index = 0
    for rob, data in robots.items():
        index += 1
        if data[1] != 0:
            data[1] -= 1
        elif data[1] == 0:
            free_robots.append(rob)

    if not free_robots:
        products.append(assem_product)
        continue
    robots[free_robots[0]][1] = robots[free_robots[0]][0]


    print(f"{free_robots[0]} - {assem_product} [{factory_time.strftime('%H:%M:%S')}]")

