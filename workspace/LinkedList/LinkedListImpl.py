from ast import While
from platform import node
from typing import Self

class Node:
    def __init__(self, val) :
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size+=1
    
    def prepend(self, val):
        newNode = Node(val)
        if self.head == None:
            self.append(val)
        else:
            firstNode = self.head
            newNode.next = firstNode
            self.head = newNode
        self.size+=1
    
    def insert(self,val, index):
        
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.prepend(val)
            return
        new_node = Node(val)
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node
        self.size+=1
        
    def search(self, val):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.val == val:
                return index
            
            temp = temp.next
            index+=1
        
        return -1
            
    def set(self, val, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.val = val

    def pop_first(self):
        val = self.head.val
        self.head = self.head.next
        self.size-=1
        return val
    
    def pop(self):

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        
        val = self.tail.val
        temp.next = None
        self.tail = temp
        self.size-=1
        return val
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    

        
    def __str__(self) -> str:
        temp = self.head
        result = ""
        while temp is not None:
            result+=str(temp.val)
            if temp.next is not None:
                result+=" -> "
            temp = temp.next
        return result 