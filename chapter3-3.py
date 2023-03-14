""" p.97 그리디 문제
 3-3. 숫자 카드 게임 """

n, m = map(int, input().split())

c = []
maximum_list = []

for _ in range(n):
    a = []

    b = list(map(int, input().split()))

    for i in range(m):
        a.append(b[i])

    c.append(a)

for i in range(len(c)):
    max_num = min(c[i])
    maximum_list.append(max_num)

print(max(maximum_list))
