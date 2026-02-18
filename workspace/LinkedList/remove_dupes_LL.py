from LinkedList.LinkedListImpl import *

def remove_dupes_from_ll(head : Node):

    temp = head
    while temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next        
        else:
            temp = temp.next

    return head