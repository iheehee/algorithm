"""
절단기 높이 보다 낮은 떡은 잘리지 않는다.
떡의 최대길이와 최소 길이의 중간 값을 절단기 높이로 설정한다.
결과 값과 손님의 요구 값을 비교하며 이진 탐색을 실시한다.

구현 사항
- 이진 탐색 코드
- 절단기 높이와 떡 길이에 따른 조건 분기
"""

n, target = map(int, input().split())

data = list(map(int, input().split()))

max_h = 0

start = 0

end = max(data)


def binary_search(start, end):
    while start <= end:
        h = (start + end) // 2
        result = 0
        for i in data:
            d = i - h
            if d < 0:
                continue
            else:
                result += d
        if result == target:
            return max_h.append(h)
        elif result > target:
            start = h + 1
        else:
            end = h - 1


binary_search(start, end)
print(max_h)
