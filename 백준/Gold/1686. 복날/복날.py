import sys
from collections import deque
input = sys.stdin.readline


v, m = map(int, input().split())

startx, starty = map(float, input().split())

endx, endy = map(float, input().split())

holes = []

while True:
    try:
        x, y = map(float, input().split())
        holes.append((x, y))
    except:
        break


def check(x, y, sx, sy): return ((x - sx) ** 2 + (y - sy) ** 2)**0.5 < v*m*60


discovered = deque()
visited = set()


def dfs(discovered):

    while discovered:

        x, y, cnt = discovered.popleft()

        if check(x, y, endx, endy):
            return f"Yes, visiting {cnt} other holes."

        for hole in holes:

            if hole not in visited and check(x, y, *hole):

                visited.add(hole)
                discovered.append((*hole, cnt+1))

    return "No."


discovered.append((startx, starty, 0))

print(dfs(discovered))
