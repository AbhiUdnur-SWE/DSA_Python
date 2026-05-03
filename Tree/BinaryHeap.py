class HeapNode:
    """HeapNode"""

    def __init__(self, size: int, heaptype: str):
        self.lst = [None] * (size + 1)
        self.heapsize = 0
        self.maxsize = size + 1
        self.heaptype = heaptype


class BinaryHeap:
    """Binary heap"""

    def __init__(self, root: HeapNode):
        self.root = root

    def heap_size(self):
        """heap size"""
        if not self.root:
            return
        else:
            return self.root.heapsize

    def level_order_traversal(self):
        """level_order_traversal"""

        if not self.root or not self.root.lst:
            return None

        for i in range(1, self.root.heapsize + 1):
            print(self.root.lst[i], end=" ")
        print()

    @staticmethod
    def heapify_tree_insert(root: HeapNode, index: int):
        """heapify_tree_insert"""

        parent = index // 2
        if index <= 1:
            return

        if root.heaptype == "min":
            if root.lst[parent] > root.lst[index]:
                root.lst[parent], root.lst[index] = root.lst[index], root.lst[parent]
            BinaryHeap.heapify_tree_insert(root, parent)

        if root.heaptype == "max":
            if root.lst[parent] < root.lst[index]:
                root.lst[parent], root.lst[index] = root.lst[index], root.lst[parent]
            BinaryHeap.heapify_tree_insert(root, parent)

    def insert(self, val: int):
        """insert"""

        if self.heap_size() + 1 == self.root.maxsize:
            return

        self.root.lst[self.heap_size() + 1] = val
        self.root.heapsize += 1
        BinaryHeap.heapify_tree_insert(self.root, self.heap_size())

    @staticmethod
    def heapify_down(root: HeapNode, index: int):
        """heapify_down"""

        leftindex = index * 2
        rightindex = (index * 2) + 1
        swapable_index = index

        if leftindex > root.heapsize:
            return

        if root.heaptype == "min":
            if root.lst[leftindex] < root.lst[swapable_index]:
                swapable_index = leftindex

            if root.lst[rightindex] < root.lst[swapable_index]:
                swapable_index = rightindex

            if swapable_index != index:
                root.lst[swapable_index], root.lst[index] = (
                    root.lst[index],
                    root.lst[swapable_index],
                )

        if root.heaptype == "max":
            if root.lst[leftindex] > root.lst[swapable_index]:
                swapable_index = leftindex

            if root.lst[rightindex] > root.lst[swapable_index]:
                swapable_index = rightindex

            if swapable_index != index:
                root.lst[swapable_index], root.lst[index] = (
                    root.lst[index],
                    root.lst[swapable_index],
                )

        BinaryHeap.heapify_down(root, swapable_index)

    def extract_node(self):
        """extract node"""

        if self.root.heapsize == 0:
            return
        extracted_node = self.root.lst[1]

        self.root.lst[1] = self.root.lst[self.root.heapsize]
        self.root.lst[self.root.heapsize] = None
        self.root.heapsize -= 1

        BinaryHeap.heapify_down(self.root, 1)
        return extracted_node

    def clear(self):
        """clear"""
        self.root.lst = None
