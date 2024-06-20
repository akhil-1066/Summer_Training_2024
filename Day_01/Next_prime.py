n = int(input())
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**(1/2))+1):
        if not n%i:
            return False
    return True
while True:
    if is_prime(n):
        print(n)
        break
    n += 1