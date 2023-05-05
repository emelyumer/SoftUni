from datetime import datetime
from collections import deque

robots = {r.split("-")[0]:[int(r.split("-")[1]), 0] for r in input().split(";")}

print(robots)