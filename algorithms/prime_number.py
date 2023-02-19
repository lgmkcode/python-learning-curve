def prime_number(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("This number is prime")
        return "1"
    else:
        print("This number is not prime")
        return "0"
    