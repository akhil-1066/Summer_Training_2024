class Node:
    def __init__(self, flag = False):
        self.children = [None] * 26
        self.flag = flag
        self.words_count = 1
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        temp = self.root
        i = 0
        while i< len(word) and temp.children[ord(word[i]) - 97]:
            prev = temp
            temp.words_count += 1
            temp = temp.children[ord(word[i]) - 97]
            i += 1
        if i>= len(word):
            temp.flag = True
            return
        while i< len(word) - 1:
            temp.children[ord(word[i]) - 97] = Node()
            temp = temp.children[ord(word[i]) - 97]
            i += 1
        temp.children[ord(word[i]) - 97] = Node(True)
    def search(self, word):
        temp = self.root
        for char in word:
            if not temp.children[ord(char) - 97]:
                return False
            temp = temp.children[ord(char) - 97]
        return temp.flag