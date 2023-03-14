n = int(input())
x, y = 1, 1
ways = input().split()

print(ways)


def add(i, way):
    if way in ["D", "R"]:
        if i == n:
            return i
        return i + 1


def sub(i, way):
    if way in ["U", "L"]:
        if i == 1:
            return i
        return i - 1


for way in ways:
    if way == "U":
        x = sub(x, way)
    if way == "D":
        x = add(x, way)
    if way == "R":
        y = add(y, way)
    if way == "L":
        y = sub(y, way)

print(x, y)

""" n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표
    for i in range(len(move_types)):
        if plan == move_types[i]:
 """
""" 오답 노트:
- 데이터 형을 만들어 놓고 for 문을 2번 돌려서 2번 확인 할 수 있다는 점을 놓쳤다.
- 코딩은 수학과는 다른 접근이 필요하다. 
    * 자료에 대한 정의 
    * for 와 if를 쓰면서 시뮬레이션을 하는 작업 
    * 초기 값에 변경 값을 대입
    * 이렇게 3가지 스텝이 있다. 기억하자.

 """
