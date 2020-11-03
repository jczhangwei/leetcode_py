#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (64.53%)
# Likes:    1356
# Dislikes: 0
# Total Accepted:    402K
# Total Submissions: 622.3K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        pr = pt = ListNode()
        while l1 or l2:
            if l1 and ((l2 and l1.val <= l2.val) or not l2):
                pt.next = l1
                l1 = l1.next
                pt = pt.next
            elif l2:
                pt.next = l2
                l2 = l2.next
                pt = pt.next


        return pr.next            
        
# @lc code=end

