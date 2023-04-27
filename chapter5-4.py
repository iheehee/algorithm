n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

result = 0


def bfs(x, y):
    global result
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y + 1] == 1:
        result += 1
        return True
    elif graph[x + 1][y] == 1:
        result += 1
        return True
    elif graph[x - 1][y] == 1:
        result += 1
        return True
    elif graph[x + 1][y] == 1:
        result += 1
        return True
    return None


for i in range(n):
    for j in range(m):
        bfs(n, m)

print(result)
