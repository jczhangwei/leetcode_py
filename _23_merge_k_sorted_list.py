import math
from queue import PriorityQueue
import queue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Sollution:
    def mergeKLists(self, lists):
        q = PriorityQueue()
        index = 0
        for l in lists:
            if l:
                q.put((l.val, index, l))
                index = index + 1

        head = p = ListNode(0)
        while not q.empty():
            val, _, n = q.get()
            p.next = ListNode(val)
            p = p.next
            if n.next:
                q.put((n.next.val, index, n.next))
                index = index + 1
        return head.next
