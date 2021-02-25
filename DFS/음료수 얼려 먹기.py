def make(ice, n, m, visited):
    count = 0
    for x in range(n):
        for y in range(m):
            if(not visited[x][y] and ice[x][y] == '0'):
                icecream(ice, x, y, visited)
                count += 1
    return count


def icecream(ice, x, y, visited):
    visited[x][y] = True
    if(x-1 >= 0):
        if(not visited[x-1][y] and ice[x-1][y] == '0'):
            icecream(ice, x-1, y, visited)
    if(y+1 < m):
        if(not visited[x][y+1] and ice[x][y+1] == '0'):
            icecream(ice, x, y+1, visited)
    if(x+1 < n):
        if(not visited[x+1][y] and ice[x+1][y] == '0'):
            icecream(ice, x+1, y, visited)
    if(y-1 >= 0):
        if(not visited[x][y-1] and ice[x][y-1] == '0'):
            icecream(ice, x, y-1, visited)


n, m = map(int, input().split())

ice = []

visited = [[False] * m for _ in range(n)]

for _ in range(n):
    ice.append([c for c in input()])

print(make(ice, n, m, visited))
