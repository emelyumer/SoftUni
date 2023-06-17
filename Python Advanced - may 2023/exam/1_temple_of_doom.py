from collections import deque

tool_list = deque([int(x) for x in input().split()])
substance_list = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while tool_list and substance_list:
    tool = tool_list.popleft()
    substance = substance_list.pop()
    check = tool * substance
    if check in challenges:
        challenges.remove(check)
        continue
    tool_list.append(tool + 1)
    if substance > 1:
        substance_list.append(substance - 1)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tool_list:
    print(f"Tools: {', '.join([str(x) for x in tool_list])}")
if substance_list:
    print(f"Substances: {', '.join([str(x) for x in substance_list])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")