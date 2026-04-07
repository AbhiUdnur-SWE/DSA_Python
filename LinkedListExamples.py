"""
# from LinkedList.MergeTwoLinkedList import *
# from LinkedList.remove_dupes_LL import remove_dupes_from_ll
# from LinkedList import remove_all_occur_from_LL
# from LinkedList import reverse_LL
# from LinkedList.CirSingLinkedList import *
# from LinkedList import CirSingLinkedList
# from LinkedList import *
# from LinkedList.DoublyLL import DoublyLL
# from LinkedList.DoublyCirLL import DoublyCirLL
# from LinkedList.LinkedListImpl import *
# from LinkedList import sum_of_two_LL
# from LinkedList.IntersectionofLL import Intersection, addSameNode
"""

if __name__ == "__main__":

    """ Merge Two LL ""
    # newLL1 = LinkedList()
    # newLL2 = LinkedList()

    # newLL1.append(1)
    # newLL1.append(2)
    # newLL1.append(4)
    # print(newLL1)

    # newLL2.append(1)
    # newLL2.append(3)
    # newLL2.append(100)
    # print(newLL2)

    # var = merge_two_llist(newLL1.head, newLL2.head)

    # while var:
    #     print(var.val, end=" ")
    #     var = var.next
    # print()
    """

    """ Remove Dupes from LL ""
    # newLL1 = LinkedList()

    # newLL1.append(1)
    # newLL1.append(1)
    # newLL1.append(2)
    # newLL1.append(3)
    # newLL1.append(3)
    # print(newLL1)

    # var = remove_dupes_from_ll(newLL1.head)
    # while var:
    #     print(var.val, end=" ")
    #     var = var.next
    # print()

    """
    
    """ Remove all occr. of val "" 
    # newLL1 = LinkedList()
    # newLL1.append(1)
    # newLL1.append(1)
    # newLL1.append(2)
    # newLL1.append(3)
    # newLL1.append(3)
    # print(newLL1)short
    # var = remove_all_occur_from_LL.remove_occr_LL(newLL1.head, 1)
    # while var:
    #     print(var.val, end=" ")
    #     var = var.next
    # print()
    
    """

    """ Reverse Linked List ""
    newLL1 = LinkedList()
    newLL1.append(1)
    newLL1.append(2)
    newLL1.append(3)
    newLL1.append(4)
    newLL1.append(5)
    print(newLL1)
    var = reverse_LL.reverse_linked_list(newLL1.head)
    while var:
        print(var.val, end=" ")
        var = var.next
    print() 
    
    """

    """ Doubly (sinmple & circular) linked list ""
    d_ll = DoublyCirLL()
    # d_ll = DoublyLL()
    d_ll.append(1)
    d_ll.append(2)
    d_ll.append(3)
    d_ll.append(4)
    d_ll.prepend(5)
    d_ll.insert(0,10000)
    d_ll.insert(6,1052)
    print(d_ll) 
    d_ll.pop_first()
    print(d_ll) 
    d_ll.pop_first()
    print(d_ll) 
    d_ll.pop()
    print(d_ll)
    d_ll.remove(1)
    print(d_ll)
    """

    # !! these examples of LL are IMPs
   
    """ SumOfTwoLL ""
    # 7 -> 1 -> 6
    # 5 -> 9 -> 2
    # ans:- 2 -> 1 -> 9
    newLL1 = LinkedList()
    newLL2 = LinkedList()
    newLL1.append(7)
    newLL1.append(1)
    newLL1.append(6)
    newLL2.append(5)
    newLL2.append(9)
    newLL2.append(2)
    a = sum_of_two_LL.SumOfTwoLL.calculate(newLL1, newLL2)
    a = a.head
    while a:
        print(a.val, end=" ")
        a = a.next
    print() 

    """

    """ Intersection ""
    # lla = LinkedList()
    # llb = LinkedList()
    # lla.append(2)
    # llb.append(3)
    # addSameNode(lla, llb,6783)
    # addSameNode(lla, llb,7689)
    # print(Intersection(lla, llb))

    """