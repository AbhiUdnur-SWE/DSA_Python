from hmac import new
from operator import ne
from platform import node
from unittest import result


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
    
class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, val:int):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size+=1
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node 
        self.size+=1
    
    def prepend(self, val:int):
        if not self.head:
            self.append(val)
            return
        
        new_node = Node(val)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.size+=1

    def get(self, index):

        if 0 > index or self.size <= index:
            return None

        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size-1, index, -1):
                curr = curr.prev
        
        return curr
    
    def set_val(self, index:int, val:int):
        node = self.get(index)
        if node:
            node.val = val
            return True
        return False

    def insert(self, index:int, val:int):
        temp = self.head

        if index == self.size:
            self.append(val)
            return

        if not self.head:
            self.append(val)
            return

        if index == 0:
            self.prepend(val)
            return

        for _ in range(index-1):
            temp = temp.next
        
        new_node = Node(val)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        self.size+=1
    
    def pop_first(self):
        temp = self.head
        temp2 = self.head.next
        if not temp.next:
            self.head = None
            self.tail = None
            return
        temp.next = None
        temp2.prev = None
        self.head = temp2
        self.size-=1

    def pop(self):
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.size-=1
        return temp

    def remove(self, index:int):
        if index == 0:
            self.pop_first()
            return
        
        if  index == self.size-1:
            self.pop()
            return

        to_remove = self.get(index)
        to_remove.prev.next = to_remove.next
        to_remove.next.prev = to_remove.prev
        to_remove.prev = None
        to_remove.next = None

    def __str__(self) -> str:
        temp =self.head
        if not temp:
            return ""
        result = " "
        while temp:
            result += str(temp.val)
            if temp.next:
                result+=" <-> "
            temp = temp.next
        return result
    