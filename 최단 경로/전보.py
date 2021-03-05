n, m, c = map(int, input().split())
INF = int(1e9)
result = 0
time = 0
distance = [INF] * (n+1)
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max = 0
for d in graph[c]:
    if d < INF and d > 0:
        result += 1
        if d > max:
            max = d

print(result, max)
