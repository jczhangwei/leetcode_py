
import math;

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = str(self.val)
        next = self.next
        while not next is None:
            s = s + "->" + str(next.val)
            next = next.next
        return s


class Sollution:
    def getList(self, list):
        node = None
        i = None
        for _, v in enumerate(list):
            if not node:
                node = ListNode(v)
                i = node
            else:
                i.next = ListNode(v)
                i = i.next
        return node

    def _addTwoNumbers(self, l1, l2):
        node = ListNode(0)
        res = node
        up = 0
        while not l1 is None or not l2 is None:
            node.next = ListNode(0)
            node = node.next
            node.val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + up
            if node.val < 10 :
                up = 0
            else:
                up = 1
            node.val = node.val % 10
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        if up != 0:
            node.next = ListNode(up)
        return res.next

    def doTest(self):
        case = [1, 1, 2, 2, 2, 3, 4, 5, 5]
        case_1 = [2, 4, 3]
        case_2 = [5, 6, 4]
        case_3 = [5]
        case_4 = [5]
        node_1 = self.getList(case_3)
        node_2 = self.getList(case_4)

        nums = list(case)
        node = self._addTwoNumbers(node_1, node_2)
        print("_addTwoNumbers: ", node)
