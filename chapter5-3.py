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
                print(ice)


make_graph(n, m)

[[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
