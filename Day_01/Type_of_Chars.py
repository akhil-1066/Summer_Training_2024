string = input()
lv = uv = lc = uc = d = s= 0
for i in string:
    if i.islower():
        if i in ['a', 'e', 'i', 'o', 'u']:
            lv += 1
        else:
            lc += 1
    elif i.isupper():
        if i in ['A', 'E', 'I', 'O', 'U']:
            uv += 1
            uc += 1
    elif 48<=ord(i)<=57:
        d += 1
    else:
        s += 1
print('Lower vowels',lv)
print('Lower consonants',lc)
print('Upper vowels',uv)
print('Upper consonants',uc)
print('Digits',d)
print('Special Char',s)