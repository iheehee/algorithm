n = int(input())

m = [input() for _ in range(n)]

sorted_number = sorted(m, reverse=True)

result = " ".join(sorted_number)

print(result)
