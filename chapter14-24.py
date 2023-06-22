n = int(input())

houses = list(map(int, input().split()))

results = []

for house in houses:
    result = 0

    for i in range(n):
        a = abs(house - houses[i])
        result = result + a

    results.append((result, house))
results.sort(key=lambda x: (int(x[0]), int(x[1])))
print(results[0][1])
