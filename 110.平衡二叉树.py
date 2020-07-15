#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (52.37%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    90K
# Total Submissions: 171.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
# 
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import *
# @lc code=start

class Solution:
    def bal(self, root: TreeNode)->int:
        if not root :
            return 0
        left = self.bal(root.left)
        if left == -1:
            return -1
        right = self.bal(root.right)
        if right == -1:
            return -1
        
        if abs(left - right) < 2:
            return max(left, right) + 1
        else:
            return -1
        
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.bal(root) != -1
        
# @lc code=end

