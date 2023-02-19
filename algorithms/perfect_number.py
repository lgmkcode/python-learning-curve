def perfect_number(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += i
    return count == n


for j in range(1, 1001):
    if perfect_number(j):
        print(j)
        