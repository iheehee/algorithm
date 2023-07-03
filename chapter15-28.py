import sys

n = int(input())

data = list(map(int, sys.stdin.readline().split()))

print(data)


def binary_search(start, end):
    result = []

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == mid:
            result.append(mid)
            break
        elif data[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    if len(result) == 0:
        return -1
    return result[0]


print(binary_search(0, n - 1))
