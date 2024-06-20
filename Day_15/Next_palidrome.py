num = int(input())
num1 = str(num)
l = len(num1)
if l & 1:
    num1 = num1[:l//2 + 1]
    num2 = int(num1 + num1[::-1][1:])
    if num2 > num:
        print(num2)
    else:
        num1 = str(int(num1) + 1)
        print(int(num1 + num1[::-1][1:]))
else:
    num1 = num1[:l//2]
    num2 = int(num1 + num1[::-1])
    if num2 > num:
        print(num2)
    else:
        num1 = str(int(num1) + 1)
        print(int(num1 + num1[::-1]))