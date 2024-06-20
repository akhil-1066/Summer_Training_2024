s = input()
n = int(input())
string = ''
ind = 0
for i in range(n):
    instruction = input()
    if instruction[0] == 'L':
        ind += int(instruction[-1])
    else:
        ind -= int(instruction[-1])
    ind = ind % len(s)
    string += s[ind]
# print(string)
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
for i in range(len(s)-len(string) + 1):
    if is_anagram(s[i:i + len(string)], string):
        print('yes')
        break
else:
    print('NO')
