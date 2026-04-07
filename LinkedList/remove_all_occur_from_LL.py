from LinkedList.LinkedListImpl import *

def remove_occr_LL(head: Node, val: int):

    dummyNode = Node(-1)
    dummyNode.next = head
    
    temp = dummyNode
    while temp.next:
        if temp.next.val == val: temp.next = temp.next.next
        else: temp = temp.next
    return  dummyNode.next

