class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class StackWithMin:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        return self.minNode.val
    
    def push(self, val:int):

        if self.minNode and val > self.minNode.val:
            self.minNode = Node(self.minNode.val, self.minNode)
        else:
            self.minNode = Node(val, self.minNode)

        self.top = Node(val=val, next=self.top)
    
    def pop(self):
        if not self.top:
            return "empty !!"
        
        temp = self.top
        self.top = self.top.next
        self.minNode = self.minNode.next
        return temp.val
    
    def __iter__(self):
        current = self.top
        while current:
            yield current.val
            current = current.next
    
    def __str__(self):
        return ' '.join([str(x) for x in self]) 
    

        
