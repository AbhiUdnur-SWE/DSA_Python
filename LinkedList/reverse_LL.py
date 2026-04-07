from LinkedList.LinkedListImpl import *

def reverse_linked_list(head : Node):

    p,c = None, head

    while c:
        nxt = c.next
        
        c.next = p
        p = c
        c = nxt

    return p