import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

count = 0

stack = []


def dfs(graph, v, visited):
    global count
    visited[v] = True
    stack.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            stack.pop()
    if len(stack) == 1:
        count += 1
        stack.pop()


dfs(graph, 1, visited)

if False in visited[1:]:
    node = visited[1:].index(False)
    dfs(graph, node + 1, visited)


print(count)


"""
해답
"""
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
