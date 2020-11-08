#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (32.59%)
# Likes:    823
# Dislikes: 0
# Total Accepted:    187.6K
# Total Submissions: 573.6K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
#
#
#

# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(vals, layer = 0, pos = 0):
    if layer <= 0:
        val_pos = 0
    else:
        val_pos = 2**layer - 1 + pos

    if len(vals) <= val_pos or vals[val_pos] == None:
        return
    root = TreeNode(vals[val_pos])
    root.left = buildTree(vals, layer + 1, 2 * pos)
    root.right = buildTree(vals, layer + 1, 2 * pos + 1)
    return root

# @lc code=start


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 左右子树的所有值必须小于low， 左右子树的所有值必须大于up
        def isValid(root: TreeNode, low, up):
            if not root:
                return True

            left = root.left
            right = root.right
            val  = root.val
            if val >= low or val <= up:
                return False

            return isValid(left, root.val, up) and isValid(right, low, root.val)

        return isValid(root, float('inf'), - float('inf'))

# @lc code=end


print(Solution().isValidBST(buildTree([5,1,4,None,None,3,6])))
print(Solution().isValidBST(buildTree([3, 1, 5, 0, 2, 4, 6])))
