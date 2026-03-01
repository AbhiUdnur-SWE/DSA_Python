from pickle import NONE

from httpx import head


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def isEmpty(self):
        return self.head == None

    def dequeue(self):

        if self.isEmpty():
            return "Empty !!"

        if self.head == self.tail:
            temp = self.head.val
            self.head = self.tail = None
            return temp

        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1
        return temp.val

    def peek(self):
        if self.head:
            return self.head.val

        return None

    def clear(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        ls = []
        while temp:
            ls.append(str(temp.val))
            temp = temp.next

        return " ".join(ls)
