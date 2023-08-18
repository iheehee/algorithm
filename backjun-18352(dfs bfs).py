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

"""정답코드"""

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)  # 방문 표시를 반드시 True False로 해야하는 것은 아님. 생각의 전환
distance[x] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 k인 도시가 없다면 -1 출력
if check == False:
    print(-1)
