n = int(input())
l, r = 0, n
def is_prime(num):
    if num<1:
        return False
    for i in range(2, int(num ** (1/2)) + 1):
        if not num % i:
            return False
    return True
while l<=r:
    if is_prime(l) and is_prime(r):
        print(l,r,'Yes')
        break
    l += 1
    r -= 1
else:
    print('No')