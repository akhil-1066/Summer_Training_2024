n = int(input())
m = n
while True:
    while n>9:
        sum_of_digits = 0
        while n:
            sum_of_digits += n%10
            n //= 10
        n = sum_of_digits
    if n in [2,3,5,7]:
        print(m)
        break
    else:
        n = m = m+1