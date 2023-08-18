"""
로봇 청소기가 있는 방은 n(세로) x m(가로) 크기
각각의 칸은 벽 또는 빈 칸
로봇 청소기는 바라보는 방향이 있다. 동, 서, 남, 북 중 하나
방은 좌표가 있다.
가장 북쪽, 가장 서쪽 좌표는 (0, 0)
가장 남쪽 가장 동쪽 (n - 1, m - 1)

최조의 로봇 청소기의 방향
0 북, 1 동, 2 남, 3 서

0 은 청소되지 않음
1 은 청소됨

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    - 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    - 반시계 방향으로 90 회전한다.
    - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    - 1번으로 돌아간다.
"""
n, m = map(int, input().split())  # N, M을 입력 받음

d = [[0] * m for _ in range(n)]  # 청소 여부를 list로 생성
x, y, direction = map(int, input().split())  # x, y, direction를 입력 받음

array = []  # 빈 칸, 벽을 입력 받음
for i in range(n):  # n 개의 rows에 대해서 각 row의 입력을 받음
    array.append(list(map(int, input().split())))  # 입력은 list 형태로 array에 append

d[x][y] = 1  # 현재 위치 청소 (0->1)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0: 위쪽 이동, 1: 오른쪽 이동, 2: 아래 이동, 3: 왼쪽 이동


def turn_left():  # 왼쪽으로 트는 함수
    global direction  # global 함수 선언
    direction -= 1  # 왼쪽으로 이동
    # 0 : 북, 1 : 동, 2 : 남, 3 : 서
    if direction == -1:  # 음수가 되는 경우,
        direction = 3  # 3으로 초기화


count = 1  # 현재 위치를 청소 했음으로 1
turn_time = 0  # 왼쪽 방향으로 회전하는 횟수 계산, 4번인 경우 다른 조건 실행
while True:
    turn_left()  # 왼쪽 방향으로 회전
    nx = x + dx[direction]  # 현재 방향으로 이동
    ny = y + dy[direction]  # 현재 방향으로 이동

    if array[nx][ny] == 0:  # 이동을 했는데, 청소하지 않은 곳이면
        array[nx][ny] = 1  # 이동한 위치에서 청소, 0->1
        x = nx  # 위치 이동
        y = ny  # 위치 이동
        count += 1  # 청소를 했음으로 1 증가
        turn_time = 0  # 왼쪽 방향 회전 횟수 0으로 초기화
        continue  # 반복

    else:  # 이동이 불가능 한 경우 왼쪽 방향 회전, 횟수 증가
        turn_time += 1

    if turn_time == 4:  # 총 4번 회전 한 경우, 네 방향 모두 청소가 되어 있거나 벽이 있는 경우
        nx = x - dx[direction]  # 바라보는 방향에서 뒤로 이동
        ny = y - dy[direction]  # 바라보는 방향에서 뒤로 이동

        if nx < 0 or n < nx or ny < 0 or m < ny:  # 뒤칸이 벽이라 후진할 수 없다면
            break
        else:  # 그렇지 않으면,
            x = nx  # 이동
            y = ny  # 이동

        turn_time = 0  # 왼쪽 방향 회전 횟수 초기화

print(count)  # count 값 출력
