#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (42.31%)
# Likes:    256
# Dislikes: 0
# Total Accepted:    74.9K
# Total Submissions: 176.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = []
        q.append(root)
        height = 1
        while(len(q) > 0):
            s = len(q)
            
            for i in range(s):
                n = q.pop(0)
                if not n.left and not n.right:
                    return height
        
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            height += 1
        
        return height
        
# @lc code=end

