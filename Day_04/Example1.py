from Single_Linked_List import List #importing Modules
l = List()
while True:
    val = int(input())
    if val==-1:
        break
    l.append(val)
l.print()
#print(l.max_length_of_sequence())
#l.pairs()
l.bubble_sort()
