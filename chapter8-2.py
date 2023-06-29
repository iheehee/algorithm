# num = int(input())

n = 30

count = 0

while n:
    print(n)
    if n == 1:
        break
    elif (n % 5) == 0:
        n = n / 5
        count += 1
    elif (n - 1) % 5 == 0:
        n -= 1
        n = n / 5
        count += 2
    elif (n % 3) == 0:
        n = n / 3
        count += 1
    elif (n - 1) % 3 == 0:
        n -= 1
        n = n / 3
        count += 2
    elif (n % 2) == 0:
        n = n / 2
        count += 1
    else:
        n -= 1
        count += 1

print(count)
