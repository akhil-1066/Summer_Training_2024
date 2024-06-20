s = input()
key = int(input())
decoded = ''
for char in s:
    val = (ord(char)-97-key)%26 + 97
    decoded += chr(val)
print(decoded) 