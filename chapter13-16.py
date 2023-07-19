"""
* 1이라는 벽은 3개를 세워야 한다.
* 바이러스 2는 최소 2개에서 최대 10개까지 늘어난다
* 안전영역은 3개 이상이어야 한다.
* 안전영역이 최대가 되는 경우의 수
 - 2차원 그래프를 만든다.
 - 값을 저장한다.
 - 방향 값을 만든다.
 - 안전 영역에 해당하는 모든 경우의 수를 구한다.
 - 겹치지 않고 벽을 3개 설치한다.
    * 
"""

n, m = map(int, input().split())

graph = []

for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

dx = [0, -1, 0, 1]  # 상, 좌, 하, 우
dy = [1, 0, -1, 0]

result = []


def virus():
    for k in range(n):  # 세로축 선택
        for i in range(m):  # 가로 축선택
            if graph[k][i] == 2:
                for j in range(4):
                    if (
                        k + dy[j] == -1
                        or k + dy[j] == n + 1
                        or i + dx[j] == -1
                        or i + dx[j] == m + 1
                    ):
                        if graph[i + dx[j]] == 0:
                            graph[i + dx[j]] = 2
                        if graph[k + dy[j]] == 0:
                            graph[k + dy[j]] = 2


def safe_zone(count):
    for k in range(n):  # 세로축 선택
        for i in range(m):  # 가로 축선택
            if graph[k][i] == 0:
                count += 1
                if k == n and i == m:
                    result.append(count)


# 벽 세우기
def dfs(count):
    for k in range(n):  # 세로축 선택
        for i in range(m):  # 가로 축선택
            if count == 0:  # 벽을 모두 세웠을 경우 안전영역 탐색
                virus()
                safe_zone(0)
            if graph[k][i] == 0:
                graph[k][i] = 1
                count -= 1
                dfs(count)


dfs(3)
print(result)

"""정답 코드"""
n, m = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            temp[i][j] == data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
