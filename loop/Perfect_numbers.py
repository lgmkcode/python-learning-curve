num = int(input("Enter a number:"))
top = 0
for i in range(num-1, 0, -1):
    if num % i == 0:
        top += i

if top == num:
    print("Number is perfect")
else:
    print("Number is not perfect")
