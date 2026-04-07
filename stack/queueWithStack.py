class QStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __str__(self):
        return str(self.stack1)

    def enqueue(self, val: int):
        self.stack1.append(val)
    

    def dequeue(self):
        for i in range(len(self.stack1)-1,-1, -1):
            self.stack2.append(self.stack1[i])
        
        self.stack2.pop()
        self.stack1 = []
        for i in range(len(self.stack2)-1,-1, -1):
            self.stack1.append(self.stack2[i])

