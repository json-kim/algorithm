def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
roads = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    roads.append((cost, a, b))

roads.sort()
sum = 0
max_cost = 0
for road in roads:
    cost, a, b = road
    if find_parent(parent, a) != find_parent(parent, b):
        sum += cost
        max_cost = cost
        union_parent(parent, a, b)

sum -= max_cost
print(sum)
