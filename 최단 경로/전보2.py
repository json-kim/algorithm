import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m, start = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    # 초기화
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
max_distance = 0
for i in graph[start]:
    if i[1] < INF and i[1] > 0:
        count += 1
        max_distance = max(max_distance, i[1])

print(count, max_distance)
