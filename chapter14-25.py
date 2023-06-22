n = 5

stages = [2, 1, 2, 6, 2, 4, 3, 3]

success = [0] * (n + 1)  # 스테이지별 도달한 플레이어 수

failure = [0] * (n + 1)  # 스테이지별 도달했으나 클리어 하지 못한 플레이어

data = []

result = []


def lose(stages, n):
    # 스테이지에 도달한 플레이어와 클리어하지 못한 플레이어를 구하는 루프
    for i in stages:
        for k in range(1, i + 1):
            # 스테이지에 도달했으나 클리어 하지 못한 플레이어 수
            if k == (n + 1):
                continue

            elif k == i:
                failure[k] = failure[k] + 1

            else:
                success[k] = success[k] + 1

    for i in range(1, n + 1):
        failure_rate = failure[i] / success[i]
        data.append((failure_rate, i))


lose(stages, n)

data.sort(key=lambda x: (-float(x[0]), float(x[1])))

print(data)
for i in range(5):
    result.append(data[i][1])

print(result)
