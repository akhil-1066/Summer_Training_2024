n = int(input())
def sum_of_digits(num):
    while num>9:
        sum_of_digits = 0
        while num:
            sum_of_digits += num%10
            num //= 10
        num = sum_of_digits
    return num
def is_prime(num):
    l = [2,1,0,0,1,0,1,0,3,2]
    return num+l[sum_of_digits(num)]
print(is_prime(n))