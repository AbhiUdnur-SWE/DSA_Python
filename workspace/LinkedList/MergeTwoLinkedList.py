from LinkedList.LinkedListImpl import *

def merge_two_llist(h1:Node, h2: Node) -> Node:

    dummyVal = Node(-1)
    temp = dummyVal

    while h1 and h2:

        if h1.val <= h2.val:
            temp.next = Node(h1.val)
            h1 = h1.next
        else:
            temp.next = Node(h2.val)
            h2 = h2.next

        temp = temp.next

    temp.next = h1 if h1 else h2

    return dummyVal.next

