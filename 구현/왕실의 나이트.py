p = str(input())

r = p[1]
c = p[0]

x = ord(c)-96
y = int(r)

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
        count += 1

print(count)
