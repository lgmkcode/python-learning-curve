print("ax^2+bx+c Enter the coefficients of the quadratic equation.1")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = (b**2)-4*a*c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print("x1:{}\nx2:{}".format(x1, x2))
