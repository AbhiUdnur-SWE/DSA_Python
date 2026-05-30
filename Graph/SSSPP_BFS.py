
class SSSPP_Graph:
    def __init__(self, gdict: dict = None):
        if gdict:
            self.gdict = gdict
        else:
            self.gdict = {}

    def bfs(self, start, end):
        """bfs"""

        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for i in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)
                # print(new_path, "----", path, "----", queue)
