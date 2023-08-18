"""
문제해석
- 치즈의 가장자리 부터 녹기 시작한다.
- dfs 를 사용하여 푼다.
조건해석
- 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하라 -> 가장자리의 치즈가 사라질 때 카운팅을 한다.
접근 방법
- visited에 대한 표시는 입력 데이터를 통해 한다. 
- 복사한 데이터를 만든다. 
- 상하좌우 안에 0이 1개 이상 존재해야 가장자리이다.
- 데이터 복사
- 구멍 탐색 -> 카운트 증가 -> 놓여져 있는 치즈 조각의 갯수 저장

"""
import sys

n, m = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

data = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]  # 상하좌우
dy = [1, -1, 0, 0]

time_count = 0
cheeze_count = 0
cheeze = []


def cheeze_count():
    global time_count
    time_count += 1
    count = 0
    for i in range(n):
        for k in range(m):
            if graph[i][k] == 1:
                data[i][k] = graph[i][k]
                count += 1
    cheeze.append(count)


def dfs(i, k):
    for i in range(n):
        for k in range(m):
            if data[i][k] == 1:
                for j in range(4):
                    # 상하좌우에 0 이 있다면 탐색
                    if data[i + dy[j]][k + dx[j]] == 0:
                        graph[i][k] = 0
                        if data[i + dy[j]][k + dx[j]] == 1:
                            dfs(i + dy[j], k + dx[j])
            if i == n - 1 and k == m - 1:
                cheeze_count()


for i in range(n):
    for k in range(m):
        dfs(i, k)

print(time_count)
cheeze.sort()
print(cheeze[1])

""" 정답 """

import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0:  # 공기면 계속 탐색하기 위해 큐에 넣음
                    q.append((nx, ny))
                elif cheeze[nx][ny] == 1:  # 치즈면 한 번에 녹이기 위해 melt에 넣음
                    melt.append((nx, ny))

    for x, y in melt:
        cheeze[x][y] = 0  # 공기와 닿은 치즈를 한 번에 녹임
    return len(melt)  # 녹인 치즈 갯수 리턴


n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])  # 전체 치즈 갯수 카운트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:  # 치즈를 다 녹였으면
        print(time, meltCnt, sep="\n")  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    time += 1
