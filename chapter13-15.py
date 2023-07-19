from collections import deque

n, m, k, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    q, w = map(int, input().split())
    graph[q].append(w)


