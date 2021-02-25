n, m = map(int, input().split())
x, y, d = map(int, input().split())
world = []
count = 0
step = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북0, 동1, 남2, 서3

for i in range(n):
    world.append(list(map(int, input().split())))

done = world[:]
rotate = 0

if(world[x][y] != 1):
    count += 1
    while True:
        d = (d + 1) % 4  # 새로 회전한 방향
        nx = x + step[d][0]
        ny = y + step[d][1]
        rotate += 1

        if(world[nx][ny] != 1 and done[nx][ny] != 1):
            x = nx
            y = ny
            count += 1
            done[nx][ny] = 1
            rotate = 0

        if(rotate == 4):
            nx = x - step[d][0]
            ny = y - step[d][1]
            if(world[nx][ny] == 1):
                break

print(count)
