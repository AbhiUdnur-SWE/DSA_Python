from Queue.CircQueueUsingList import CircularQueue
from Queue.QueueLL import Queue
from collections import deque
import queue as q
if __name__ == "__main__":

    """
    # cq = CircularQueue(3)
    # cq.enqueue(1)
    # cq.enqueue(2)
    # cq.enqueue(3)
    # print(cq)
    # cq.dequeue()
    # cq.dequeue()
    # cq.dequeue()
    # print(cq)
    # print(cq.peek())
    """
 
    """
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    """

    # dq = deque(maxlen=3)
    # dq.append(1)
    # dq.append(2)
    # dq.append(3)

    qu = q.Queue()
    qu.put(1)
    qu.put(1)
    qu.put(1)
    print(qu.qsize())


