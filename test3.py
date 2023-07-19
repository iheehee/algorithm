"""
n 도시의 개수
m 도로의 개수
k 거리의 정보
x 출발도시의 정보

거리의 정보가 주어진다.
출발도시로 부터 해당 거리 만큼 갈수 있는 도시를 구하라

- 전역변수로 거리정보를 선언한다.
- 탐색을 할 때마다 탐색거리를 카운팅한다. 
- 거리정보와 탐색거리가 같은 노드가 정답이다. 
"""


n, m, k, x = map(int, input().split())

data = [0] * (n + 1)

graph = [[] for _ in range(m + 1)]

for _ in range(1, m + 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

results = []

print(data)


def DFS(k, x, count):
    # 탐색거리를 선언한다.

    for i in graph[x]:
        if count > k:
            break
        elif count <= k:
            count += 1
            results.append((count, i))
            DFS(k, i, count)
            count -= 1


DFS(k, x, 0)

print(results)

if len(results) == 0:
    print(-1)
else:
    for result in results:
        data[result[1]] += 1
    for i in range(len(data)):
        if data[i] == 1:
            print(i)


