#
# @lc app=leetcode.cn id=161 lang=python3
#
# [161] 相隔为 1 的编辑距离
#
# https://leetcode-cn.com/problems/one-edit-distance/description/
#
# algorithms
# Medium (32.84%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 13.2K
# Testcase Example:  '"ab"\n"acb"'
#
# 给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。
# 
# 注意：
# 
# 满足编辑距离等于 1 有三种可能的情形：
# 
# 
# 往 s 中插入一个字符得到 t
# 从 s 中删除一个字符得到 t
# 在 s 中替换一个字符得到 t
# 
# 
# 示例 1：
# 
# 输入: s = "ab", t = "acb"
# 输出: true
# 解释: 可以将 'c' 插入字符串 s 来得到 t。
# 
# 
# 示例 2:
# 
# 输入: s = "cab", t = "ad"
# 输出: false
# 解释: 无法通过 1 步操作使 s 变为 t。
# 
# 示例 3:
# 
# 输入: s = "1203", t = "1213"
# 输出: true
# 解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。
# 
#

# @lc code=start
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
# @lc code=end

