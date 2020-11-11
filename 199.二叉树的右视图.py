#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.40%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    73K
# Total Submissions: 113.2K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
#
#
#
from tools import *
from typing import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 深度优先
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        left_in_deep = {0:root.val}
        stack = [(0, root)]
        while stack:
            depth, node = stack.pop()
            if node:
                if left_in_deep.get(depth) is None:
                    left_in_deep[depth] = node.val
                
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
            
        return [left_in_deep[i] for i in range(len(left_in_deep))]
                    
# 广度优先
class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        left_in_deep = {0:root.val}
        stack = [(0, root)]
        while stack:
            depth, node = stack.pop(0)
            if node:
                left_in_deep[depth] = node.val
                
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
            
        return [left_in_deep[i] for i in range(len(left_in_deep))]
                    

        
        
        # @lc code=end


print(Solution().rightSideView(buildTree([1, 2, 3, None, 5, None, 4])))
print(Solution2().rightSideView(buildTree([1, 2, 3, None, 5, None, 4])))
