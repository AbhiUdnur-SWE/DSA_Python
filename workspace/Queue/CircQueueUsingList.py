# isFull(), isEmpty(), deque(), enque(), delete(), peek()

class CircularQueue:
    def __init__(self, maxSize: int):
        self.items = [None] * maxSize
        self.maxSize = maxSize
        self.top = -1
        self.start = -1

    def isFull(self):
        if self.top + 1 == self.start:
            return True

        if self.top + 1 == self.maxSize and self.start == 0:
            return True
        return False

    def enqueue(self, val: int):
        if self.isFull():
            return "Full !!"

        else:
            if self.start == -1:
                self.start += 1

            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1

            self.items[self.top] = val
            return f"{val} added"

    def dequeue(self):
        if self.isEmpty():
            return "empty!!"

        else:
            removed = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = self.top = -1

            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return removed

    def isEmpty(self):
        return self.top == -1

    def peek(self):
        return self.items[self.start] if not self.isEmpty() else "empty!!"

    def clear(self):
        self.items = [None]*self.maxsize
        self.start = -1
        self.top = -1
    
    def __str__(self):
        vals = [str(x) for x in self.items]
        return " ".join(vals)
