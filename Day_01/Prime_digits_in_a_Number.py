n = int(input())
while n:
    num = n%10
    n = n//10
    if num in [2, 3, 5, 7]:
        count += 1
print(count)