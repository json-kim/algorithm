from collections import deque

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
    lec = list(map(int, input().split()))
    time[i] = lec[0]
    for j in range(1, len(lec)-1):
        graph[lec[j]].append(i)
        indegree[i] += 1

print('graph:', graph)
print('time:', time)


def topolgy_sort():
    result = [0] * (n+1)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] += time[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], time[i] + result[now])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])


topolgy_sort()
