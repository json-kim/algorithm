graph = [[] for _ in range(3)]

# 노드 0
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1
graph[1].append((0, 7))

# 노드 2
graph[2].append((0, 5))

print(graph)
