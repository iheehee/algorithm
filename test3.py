"""
도시의 개수 n
간선의 개수 m
거리의 정보 k
출발도시의 번호 x
간선의 값 1
특정 도시 x로 부터 출발 -> 최단거리가 정확히 k인 모든 도시들의 번호를 출력하시오

최단거리가 k인 모든 도시의 번호를 오름차순 정렬
최단거리 k인 도시가 하나도 존재하지 않으면 -1 출력    
"""
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(m + 1)]

visited = [False] * (m + 1)

for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a].append(b)

count = [0] * (n + 1)
result = []


def bfs(start):
    q = deque([start])

    visited[start] = True
    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                count[i] = count[v] + 1
                if count[i] == k:
                    result.append(i)


bfs(x)

print(count)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)
