"""
문제 해석
- 주어진 입력으로 그래프를 만들고 결과 값을 탐색하는 문제
- 결과는 인접 행렬 방식으로 출력

조건 해석
- (1, 2) 은 1에서 2로 가는 간선이 있는지에 대한 질문이다.
- 간선이 있는지에 대해서는 BFS로 탐색한다.

접근
- 입력 값을 기반으로 graph를 만든다.
- 0으로 초기화된 결과값 행렬을 만든다.
- 간선이 있다면 결과 값 행렬의 값을 1로 변환하고 해당 정점을 큐에 넣는다.
"""

n = int(input())

data = []

graph = [[]] * n

result = [[0] * n for _ in range(n)]

for _ in range(n):
    a = list(map(int, input().split()))
    data.append(a)

for i in range(n):
    for k in range(len(data[i])):
        if data[k] == 1:
            graph[i].append(k)

def DFS():
    for i in range(n):
        for k in range(n):
            if data[i][k] == 1:
                for j in graph[i]:
"""
피지컬
- graph와 관련된 코드를 2번이나 생성할 필요가 없다.
- bfs 코드 구현이 아직 서투르다.
- bfs 개념에 대한 응용력이 부족하다.

"""


""" 정답 """
from collenctions import deque

n= int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)

"""DFS로 푼 답"""

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
 
def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
 

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    