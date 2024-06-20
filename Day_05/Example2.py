from Double_Linked_List import List
l = List()
s = '{[(]}'
for char in s:
    l.append(char)
print(l.is_balance())