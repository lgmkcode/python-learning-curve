num = (input("Enter a number:"))
num1 = int(num)
num2 = num1
num3 = 0
for i in range(0, len(num)):
    num3 += (num1 % 10) ** len(num)
    num1 //= 10
if num3 == num2:
    print("The number is armstrong")
else:
    print("The number is not armstrong")
