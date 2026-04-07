from LinkedList.LinkedListImpl import *

class SumOfTwoLL:
    def __init__(self):
        pass

    def calculate(llA : LinkedList, llB:LinkedList)-> Node :
        ll = LinkedList()

        tempA = llA.head
        tempB = llB.head
        carry = 0
        while tempA or tempB:
            result = carry
            if tempA:
                result+=tempA.val
                tempA = tempA.next
            if tempB:
                result+=tempB.val
                tempB = tempB.next

            ll.append(result % 10)
            carry = result // 10
        
        return ll

