def perfect_divisors(n):
    list1 = []
    for i in range(1, n+1):
        if n % i == 0:
            list1.append(i)
    return list1


while True:
    num = input("Enter a number:")
    if num == 'q':
        print("Exited the program.")
        break
    else:
        print("Perfect divisors list:", perfect_divisors(int(num)))
