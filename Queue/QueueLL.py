
class Node:
    """Node for queue linked list."""
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Queue:
    """Queue implementation using linked list."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, val):
        """Add an element to the end of the queue."""
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def is_empty(self):
        """Check if the queue is empty."""
        return self.head == None

    def dequeue(self):

        if self.is_empty():
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
