from collections import deque

n, m = map(int, input().split())

ice_case = [list(map(int, input())) for _ in range(n)]

graph = [[]]

queue = deque()


def make_graph(n, m):
    for i in range(n):
        for j in range(m):
            ice = []
            if ice_case[i][j] == 0:
                # 상하좌우에 0이 있는지 탐색
                if j in [0, m - 1]:  # 행렬의 양 끝일 경우
                    if j == 0:  # 좌쪽 끝이면 우로만 간다
                        if ice_case[i][j + 1] == 0:  # 우
                            ice.append((i, j + 1))
                    elif j == m - 1:  # 우쪽 끝이면 좌로만 간다
                        if ice_case[i][j - 1] == 0:  # 좌
                            ice.append((i, j - 1))
                else:
                    if ice_case[i][j - 1] == 0:  # 좌
                        ice.append((i, j - 1))
                    if ice_case[i][j + 1] == 0:  # 우
                        ice.append((i, j + 1))

                if i in [0, n - 1]:
                    if i == 0:
                        if ice_case[i + 1][j] == 0:  # 하
                            ice.append((i + 1, j))
                    elif i == n - 1:
                        if ice_case[i - 1][j] == 0:  # 상
                            ice.append((i - 1, j))
                else:
                    if ice_case[i + 1][j] == 0:  # 하
                        ice.append((i + 1, j))
                    if ice_case[i - 1][j] == 0:  # 상
                        ice.append((i - 1, j))
                graph.append(ice)


visited = ice_case
ice_count = 0


def bfs(graph, ice_case):
    queue = deque()

    for i in range(len(graph)):
        for j, k in graph[i]:
            if visited[j][k] == 0:
                queue.append((j, k))
                visited[j][k] = 1
    

[[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# 그래프값
[(0, 1), (1, 0)]
[(0, 0), (1, 1)]
[]
[(1, 1), (0, 0)]
[(1, 0), (1, 2), (0, 1)]
[(1, 1)]
[(3, 1)]
[(3, 0), (3, 2)]
[(3, 1), (3, 3)]

# 교재 정답
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return None


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)  # 정답 출력
