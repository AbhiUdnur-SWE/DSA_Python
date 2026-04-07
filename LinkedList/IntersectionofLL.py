
from LinkedList.LinkedListImpl import LinkedList, Node


def Intersection(lla:LinkedList, llb:LinkedList):
    if lla.tail is not llb.tail:
        return False
    
    shorter = lla if lla.size < llb.size else llb
    longer = llb if lla.size < llb.size else lla

    diff = longer.size - shorter.size
    longN = longer.head
    shortN = shorter.head

    for _ in range(diff):
        longN = longN.next
    
    while longN is not shortN:
        longN = longN.next
        shortN = shortN.next
    
    return longN.val

def addSameNode(lla:LinkedList, llb:LinkedList, val:int):
    node = Node(val)

    lla.tail.next = node
    lla.tail  = node
    
    llb.tail.next = node
    llb.tail  = node