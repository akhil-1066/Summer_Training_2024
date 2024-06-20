n = int(input())
l = [input()[:n] for i in range(n)]
s = input()
for i, char in enumerate(s):
    if char not in l[i%n]:
        print(False)
        break
else:
    print(True)