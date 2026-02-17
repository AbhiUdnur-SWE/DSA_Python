from hmac import new
from traceback import print_exc
from LinkedList.LinkedListImpl import *

if __name__ == "__main__":
    newLL = LinkedList()
    newLL.append(465)
    newLL.append(2345)
    newLL.append(234545415)
    newLL.append(54)
    newLL.prepend(846343)
    newLL.insert(152,0)
    # print(newLL)
    # newLL.set(40, 0)
    print(newLL)
    newLL.pop_first()
    print(newLL)
    newLL.pop()
    print(newLL)
    newLL.pop()
    print(newLL)
    newLL.clear()
    print(newLL)