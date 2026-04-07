from LinkedList.LinkedListImpl import *

def is_pallindrome(head: Node):
    slow = fast = head

    # find middle
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    

    # reverse second half
    temp = None
    while slow:
        nxt = slow.next
        slow.next = temp
        temp = slow
        slow = nxt
    
    while temp:

        if temp.val != head.val:
            return False
        temp.next
        head.next
    
    return True