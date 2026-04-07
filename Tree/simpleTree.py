class SimpleTree:
    def __init__(self, data: int, children=None):
        self.data = data
        self.children = children if not children else []

    def AddChild(self, root):
        self.children.append(root)

    def __str__(self, level=0):
        res = " " * level + f"{self.data}\n"
        for i in self.children:
            res += i.__str__(level + 1)
        return res
