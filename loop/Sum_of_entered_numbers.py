sum1 = 0
while True:
    num = input("Enter a number:")
    if num == 'q':
        break
    else:
        sum1 += int(num)
print("sum of entered numbers ", sum1)
