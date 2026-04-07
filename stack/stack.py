class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, val: int):
        node = Node(val)
        node.next = self.top
        self.top = node

        self.length += 1

    def pop(self):
        if self.top:
            popped = self.top
            self.top = self.top.next
            popped.next = None
            self.length -= 1
            return popped
        return -1
    
    def peek(self):
        return self.top
    
    def isEmpty(self):
        return self.length == 0
    
    def clear(self):
        self.top = None
        self.length = 0    
