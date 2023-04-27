n = int(input())

m = []

result = []

for i in range(n):
    name_score = input().split()
    m.append(name_score)

sorted_score = sorted(m, key=lambda x: x[1])

for i in range(n):
    result.append(sorted_score[i][0])

print(" ".join(result))
