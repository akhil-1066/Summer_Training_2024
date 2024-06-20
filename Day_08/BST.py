class node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Bst:
    def __init__(self):
        self.root = None
    def create(self, val):
        if not self.root:
            self.root = node(val)
        else:
            temp = self.root
            while temp:
                previous = temp
                if temp.val > val:
                    temp = temp.left
                elif temp.val < val:
                    temp = temp.right
                else:
                    return 'Data already Exist'
            if previous.val > val:
                previous.left = node(val)
            else:
                previous.right = node(val)
    def inorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                print(node.val, end = ' ')
                Traverse(node.right)
        Traverse(self.root)
        print()
    def preorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                print(node.val, end = ' ')
                Traverse(node.left)
                Traverse(node.right)
        Traverse(self.root)
        print()
    def postorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                Traverse(node.right)
                print(node.val, end = ' ')
        Traverse(self.root)
        print()
