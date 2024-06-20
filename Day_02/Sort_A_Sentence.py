s = list(input().split())
keys = [int(chars[-1]) for chars in s]
s = [chars[:-1] for chars in s]
ans = [chars for key, chars in sorted(zip(keys,s))]
print(' '.join(ans))