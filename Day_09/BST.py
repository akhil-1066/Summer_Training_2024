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
            return
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
    def height(self, Node):
        if not Node:
            return 0
        return 1 + max(self.height( Node.left), self.height(Node.right))
    def is_balance(self):
        def balance(Node):
            if not Node:
                return 0
            height1 = balance(Node.left)
            if height1 == -1:
                return -1
            height2 = balance(Node.right)
            if height2 == -1:
                return -1
            if abs(height1 - height2)>1:
                return -1
            return max(height1, height2) + 1
        return True if balance(Node = self.root) != -1 else False
    def leaf_node_count(self):
        def leaf_node(Node = self.root):
            if not (Node.left or Node.right):
                return 1
            if not Node.left:
                return leaf_node(Node.right)
            if not Node.right:
                return leaf_node(Node.left)
            return leaf_node(Node.left) + leaf_node(Node.right)
        return leaf_node()
    def leaf_node_sum(self):
        def leaf_node(Node = self.root):
            if not (Node.left or Node.right):
                return Node.val
            if not Node.left:
                return leaf_node(Node.right)
            if not Node.right:
                return leaf_node(Node.left)
            return leaf_node(Node.left) + leaf_node(Node.right)
        return leaf_node()
    def Search(self, val):
        def search(Node = self.root):
            if not Node:
                return False
            if Node.val == val:
                return True
            if Node.val>val:
                return search(Node.left)
            return search(Node.right)
        return search()
    def finddepth(self, val):
        def depth(Node = self.root):
            if not Node:
                return float('-inf')
            if Node.val == val:
                return 0
            if Node.val>val:
                return depth(Node.left) + 1
            return depth(Node.right) + 1
        Depth = depth()
        return Depth if Depth != float('-inf') else 'Not Found'
    def summ(self, Node):
        if not Node:
            return 0
        return Node.val + self.summ(Node.left) + self.summ(Node.right)
    def Evensum(self, Node):
        if not Node:
            return 0
        return  (Node.val if not Node.val & 1 else 0) + self.Evensum(Node.left) + self.Evensum(Node.right)
    def Oddsum(self, Node):
        if not Node:
            return 0
        return  (Node.val if Node.val & 1 else 0) + self.Oddsum(Node.left) + self.Oddsum(Node.right)
    def diff(self):
        def absdiff(Node = self.root):
            if not Node:
                return 0
            return  (Node.val if Node.val & 1 else -Node.val) + absdiff(Node.left) + absdiff(Node.right)
        return abs(absdiff())
    
    def leftview(self):
        level_list = []
        def view(Node = self.root, level = 0):
            if not Node:
                return []
            val = []
            if level not in level_list:
                level_list.append(level)
                val = [Node.val]
            return val + view(Node.left, level + 1) + view(Node.right, level + 1) 
        return view()
    
    def rightview(self):
        level_list = []
        def view(Node = self.root, level = 0):
            if not Node:
                return []
            val = []
            if level not in level_list:
                level_list.append(level)
                val = [Node.val]
            return val + view(Node.right, level + 1) + view(Node.left, level + 1) 
        return view()
    
    def topview(self):
        level_list = []
        def view(Node = self.root, level = 0):
            if not Node:
                return []
            val = []
            if level not in level_list:
                val = [Node.val]
                level_list.append(level)
            return val + view(Node.left, level - 1) + view(Node.right, level + 1)
        return view()
        
    def topviewbfs(self):
        top_view_list = {}
        def view(Node = self.root):
            node_list = [(self.root,0)]
            i = 0
            while i<len(node_list):
                Node, level = node_list[i]
                if not Node:
                    i += 1
                    continue
                if level not in top_view_list:
                    top_view_list[level] = Node.val
                node_list += [(Node.left, level - 1), (Node.right, level + 1)]
                i += 1
        view()
        return [top_view_list[key] for key in sorted(top_view_list)]
    
    def bottomview(self):
        def view(Node = self.root, pos = 0, posl = []):
            if not Node:
                return [], posl
            l1, posl1 = view(Node.left, pos - 1)
            l2, posl2 = view(Node.right, pos + 1)
            l = []
            if pos not in posl1 + posl2:
                l = [Node.val]
            return l + l1 + l2 , posl1 + posl2 + [pos]
        return view()[0]
    
    def bottomviewbfs(self):
        bottom_view_list = {}
        def view(Node = self.root):
            node_list = [(self.root,0)]
            i = 0
            while i<len(node_list):
                Node, level = node_list[i]
                if not Node:
                    i += 1
                    continue
                bottom_view_list[level] = Node.val
                node_list += [(Node.left, level - 1), (Node.right, level + 1)]
                i += 1
        view()
        return [bottom_view_list[key] for key in sorted(bottom_view_list)]