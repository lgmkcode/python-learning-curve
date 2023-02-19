def square(n):
    return n ** 2


def hello(name):
    print("Name:", name)


def sum1(a, b, c):
    print("Sum of a, b and c:", a+b+c)


def factorial(n1):
    n2 = 1
    n1 = int(n1)
    while n1 > 0:
        n2 *= n1
        n1 -= 1
    return n2


def factorial1(n1):
    n2 = 1
    while n1 > 0:
        n2 *= n1
        n1 -= 1
    return n2


print(square(5))
print(hello("jesse"))
print(sum1(11, 12, 1))
print(factorial(5))
