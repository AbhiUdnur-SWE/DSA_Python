from inspect import stack


class PlateStack:
    def __init__(self, capasity: int):
        self.capasity = capasity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def push(self, val: int):
        if len(self.stacks) != 0 and len(self.stacks[-1]) < self.capasity:
            self.stacks[-1].append(val)
        else:
            self.stacks.append([val])

    def pop(self):

        if len(self.stacks) != 0 and len (self.stacks[-1]) == 0:
            self.stacks.pop()
        
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()