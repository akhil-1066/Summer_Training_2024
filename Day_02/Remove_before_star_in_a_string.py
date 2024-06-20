s = input()
stack = []
for char in s:
    if char != '*':
        stack.append(char)
    elif stack:
        stack.pop()
print(''.join(stack))