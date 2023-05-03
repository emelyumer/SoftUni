from collections import deque
box_of_clothes = input().split()
capacity_one_rack = int(input())
capacity_used_rack = capacity_one_rack
used_boxes = 1
while box_of_clothes:
    cloth = int(box_of_clothes[-1])
    if capacity_used_rack >= cloth:
        capacity_used_rack -= cloth
        box_of_clothes.pop()

    else:
        used_boxes += 1
        capacity_used_rack = capacity_one_rack
        capacity_used_rack -= cloth
        box_of_clothes.pop()
print(used_boxes)