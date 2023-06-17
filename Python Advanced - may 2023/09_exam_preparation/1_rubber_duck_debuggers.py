from collections import deque
duck_rate = {60: "Darth Vader Ducky", 120: "Thor Ducky", 180: "Big Blue Rubber Ducky", 240: "Small Yellow Rubber Ducky"}
completed = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

time_task_list = deque([int(x) for x in input().split()])
number_tasks_list = deque([int(x) for x in input().split()])

while time_task_list and number_tasks_list:
    time = time_task_list.popleft()
    task = number_tasks_list.pop()
    duck = time * task
    for rate, name in duck_rate.items():
        if duck <= rate:
            completed[name] += 1
            break
    else:
        time_task_list.append(time)
        number_tasks_list.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in completed.items():
    print(f"{key}: {value}")

