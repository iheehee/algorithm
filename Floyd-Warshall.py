"""
구현
- 2차원 리스트에 '최단거리'정보를 저장한다
- 노드와 노드 사이의 모든 경로를 고려
- 노드의 개수가 N개 일때 N번 만큼 단계를 반복 O(N**2)의 시간이 소요
- 각 단계의 최소값으로 리스트를 갱신
- 총 시간 복잡도 O(n**3)

"""
INF = int(1e9)  # 무한을 의미

n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]


# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
