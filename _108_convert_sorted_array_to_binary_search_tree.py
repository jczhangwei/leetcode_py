
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Sollution:
    def toBST(self, nums, start, end):
        if end <= start:
            return

        m = math.floor((start + end) / 2)
        node = TreeNode(nums[m])
        if m > start:
            node.left = self.toBST(nums, start, m)
        if m + 1 < end:
            node.right = self.toBST(nums, m + 1, end)    
        return node
        

    def doTest(self):
        case = [-10,-3,0,5,9]
        nums = list(case)
        node = self.toBST(nums, 0, len(nums))
        print("sortedArrayToBST: ", node)
