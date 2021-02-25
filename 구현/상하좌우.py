n = int(input())
moving = input().split()

x, y = 1, 1
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
steps = ['U', 'D', 'R', 'L']

for step in moving:
    for i in range(len(steps)):
        if(step == steps[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    if(nx < 1 or nx > n or ny < 1 or ny > n):
        continue
    x = nx
    y = ny

print(x, y)
