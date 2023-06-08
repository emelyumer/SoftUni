from collections import deque
def fill_the_box(height, length, width, *cubes):
    cubes = deque(cubes)
    size = height * length * width
    while cubes[0] != "Finish":
        current_cubes = int(cubes.popleft())
        if size >= current_cubes:
            size -= current_cubes
        else:
            difference = abs(size - current_cubes)
            cubes.appendleft(difference)
            size -= (current_cubes - difference)
            cubes.pop()
            return f"No more free space! You have {sum(cubes)} more cubes."
    return f"There is free space in the box. You could put {size} more cubes."


print(fill_the_box(5, 5,
2, 40, 11, 7, 3, 1, 5,
"Finish"))
print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))
