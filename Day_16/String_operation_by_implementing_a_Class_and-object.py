'''
Input:
        8
        1 school
        1 word
        1 world
        1 scholar
        4 word
        2 word
        2 wood
        3 sch
'''

class Problem:
    def __init__(self):
        self.words = set()
    def insert(self, word):
        self.words.add(word)
    def search(self, word):
        return word in self.words
    def is_prefix(self, word):
        for word1 in self.words:
            if word1.startswith(word):
                return True
        return Falses
    def remove(self, word):
        if word in self.words:
            self.words.remove(word)
obj = Problem()
n = int(input())
for _ in range(n):
    ip = input().split()
    if ip[0] == '1':
        obj.insert(ip[1])
    elif ip[0] == '2':
        print(obj.search(ip[1]))
    elif ip[0] == '3':
        print(obj.is_prefix(ip[1]))
    else:
        obj.remove(ip[1])