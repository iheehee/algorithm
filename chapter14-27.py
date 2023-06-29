"""
이진탐색
"""

end, target = map(int, input().split())

data = list(map(int, input().split()))


def binary_search(data, start, end, target):
    count = 0
    if data[0] > target or data[end] < target:
        return -1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            count += 1
            del data[mid]
            end = end - 1
            continue
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return count


print(binary_search(data, 0, end - 1, target))
