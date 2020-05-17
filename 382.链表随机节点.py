#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#
# https://leetcode-cn.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (56.62%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 8.5K
# Testcase Example:  '["Solution","getRandom"]\n[[[1,2,3]],[]]'
#
# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
# 
# 进阶:
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？
# 
# 示例:
# 
# 
# // 初始化一个单链表 [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
# solution.getRandom();
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.        """
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

