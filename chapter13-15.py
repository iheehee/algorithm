from collections import deque

n, m, k, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    q, w = map(int, input().split())
    graph[q].append(w)

visited = [False] * (n + 1)

result = []

distance = [0] * (n + 1)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1
                if distance[i] == k:
                    result.append(i)


bfs(graph, start, visited)
result.sort()
for i in result:
    if distance[i] == k:
        print(i)

if len(result) == 0:
    print(-1)
