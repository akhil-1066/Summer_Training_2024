class Node:
    def __init__(self, flag = False):
        self.flag = flag
        self.children = {}
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        temp = self.root
        i = 0
        while i< len(word) and word[i] in temp.children:
            temp = temp.children[word[i]]
            i += 1
        if i >= len(word):
            temp.flag = True
            return
        while i< len(word):
            temp.children[word[i]] = Node()
            temp = temp.children[word[i]]
            i += 1
        temp.flag = True
    def search(self, word):
        temp = self.root
        for char in word:
            if not (temp and char in temp.children):
                return False
            temp = temp.children[char]
        return temp.flag
    def is_prefix(self, word):
        temp = self.root
        for char in word:
            if not (temp and char in temp.children):
                return False
            temp = temp.children[char]
        return True
    def words_starts_with(self, word):
        temp = self.root
        def find_words(node, string = []):
            res = []
            if node.flag == 1:
                res.append(''.join(string))
            for char in node.children:
                res += find_words(node.children[char], string + [char])
            return res
        
        for char in word:
            prev = temp
            if char not in temp.children:
                return 'No Words'
            temp = temp.children[char]
        ans = find_words(prev.children[char])
        return [word + chars for chars in ans]
    def max_len_word_starts_with(self, words):
        def find_words(node, string = []):
            res = ''
            if not node.children:
                return (''.join(string))
            for char in node.children:
                res = max(res, find_words(node.children[char], string + [char]),key = lambda x : len(x))
            return res
        ans = []
        for word in words:
            temp = self.root
            for char in word:
                prev = temp
                if char not in temp.children:
                    ans.append('No Word starts with - ' + word)
                    break
                temp = temp.children[char]
            else:
                ans.append(word + find_words(prev.children[char]))
        return ans
    
    def lexicographically_max_len_word_starts_with(self, words):
        
        def find_words(node, string = [], res = ''):
            if not node.children:
                return (''.join(string))
            for char in node.children:
                res1 = find_words(node.children[char], string + [char], res)
                if len(res1) > len(res):
                    res = res1
                elif len(res1) == len(res):
                    res = min(res, res1)
            return res
        ans = []
        for word in words:
            temp = self.root
            for char in word:
                prev = temp
                if char not in temp.children:
                    ans.append('No Word starts with - ' + word)
                    break
                temp = temp.children[char]
            else:
                ans.append(word + find_words(prev.children[char]))
        return ans
