from asyncio import new_event_loop
from curses.panel import new_panel
from hmac import new


class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None


class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def append(self, val:int):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.size+=1
    
    def prepend(self, val:int):
        if not self.head:
            self.append(val)
            return
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.size+=1


    def insert(self, index:int, val:int):
        if index == 0:
            self.prepend(val)
            return
        if index == self.size - 1:
            self.append(val)
            return
        
        temp = self.head
        new_node = Node(val)
        for _ in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node   

        self.size+=1 

    def search(self,val:int):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.val == val:
                return index
            temp = temp.next
            if temp == self.head:
                break
            index+=1
        return -1 
    
    def pop_first(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
            return
        popped_node = self.head
        self.head = self.head.next
        self.tail.next = self.head
        popped_node.next = None
        self.size-=1        

    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
            return

        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        
        temp.next = self.head
        self.tail.next = None
        self.tail = temp
        self.size = 0

    def __str__(self):
        temp = self.head
        result = ""

        while temp is not None:
            result+=str(temp.val)
            temp = temp.next
            if temp == self.head:
                break
            result += " -> "
        
        return result

