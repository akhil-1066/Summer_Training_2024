class node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class List:
    def __init__(self):
        self.head = self.next = None
        self.len = 0
        
    def append(self, val):
        if not self.head:
            self.head = self.tail = node(val)
        else:
            self.tail.next = node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.len += 1
        
    def add_at_front(self, val):
        if not self.head:
            self.head = self.tail = node(val)
        else:
            self.head.prev = node(val)
            self.head.prev.next = self.head
            self.head = self.head.prev
        self.len += 1
        
    def pop(self):
        if not self.head:
            return 'Empty List'
        if self.head == self.tail:
            val = self.head.val
            self.head = self.tail = None
            return val
            return
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.len -= 1
        return val
    
    def delete_at_front(self):
        if not self.head:
            return 'Empty List'
        if self.head == self.tail:
            self.head = self.tail = None
        val = self.head.val
        self.head = self.head.next
        self.head.prev = None
        self.len -= 1
        return val
    
    def search(self, val):
        left, right = self.head, self.tail
        while left.prev != right:
            if left.val == val or right.val == val:
                return True
            if left == right:
                break
            left = left.next
            right = right.prev
        return False
    
    def even_or_odd(self):
        left, right = self.head, self.tail
        while True:
            if left.next == right:
                return 'Even'
            if left == right:
                return 'Odd'
            left = left.next
            right = right.prev
        
    def is_palindrome(self):
        left, right = self.head, self.tail
        while left.prev != right:
            if left.val != right.val:
                return False
            if left == right:
                break
            left = left.next
            right = right.prev
        return True
    
    def change(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        self.tail.next = self.head
        self.head.prev = self.tail
        self.tail = slow.prev
        slow.prev.next = None
        self.head = slow
        self.head.prev = self.tail.next = None
    
    def change_sides(self):
        first, second = self.head, self.head.next
        self.head = second
        self.head.prev = None
        while True:
            third = second.next
            second.next, first.prev = first, second
            if not third or not third.next:
                break
            third.next.prev = first
            first.next = third.next
            first = third
            second = third.next
        if second == self.tail:
            self.tail = first
            self.tail.next = None
        else:
            self.tail.prev = first
            first.next = self.tail
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.val, end = ' ')
            temp = temp.next
        print()

    def print_reverse(self):
        temp = self.tail
        while temp:
            print(temp.val, end = ' ')
            temp = temp.prev
        print()
    def length(self):
        return self.len
    def is_balance(self):
        temp = self.head
        pos = 0
        stack = List()
        while temp:
            pos += 1
            if temp.val in '({[':
                stack.append(temp.val)
                temp = temp.next
                continue
            elif not stack.length():
                return pos
            val = stack.pop()
            if ( temp.val == ')' and val != '(' ) or ( temp.val == ']' and val != '[' ) or (temp.val == '}' and val != '{'):
                return pos
            temp = temp.next
        return -1
    def print_sum(self):
        def Traverse(node, even = 0, odd = 0):
            if not node:
                return abs(odd - even)
            if node.val & 1:
                odd += node.val
            else:
                even += node.val
            return Traverse(node.next, even, odd)
        return Traverse(self.head)
    def prime_count(self):
        def is_prime(val, end, current = 2):
            if val < 2:
                return False
            if current>end:
                return True
            if not val % current:
                return False
            return is_prime(val, end, current + 1)
                     
        def Traverse(node, count = 0):
            if not node:
                return count
            count += 1 if is_prime(node.val, int(node.val ** (1/2))) else 0
            return Traverse(node.next, count)
        return Traverse(self.head)
         
                