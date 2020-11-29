#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.01%)
# Likes:    711
# Dislikes: 0
# Total Accepted:    128.4K
# Total Submissions: 168.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

from typing import *
# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back(t_nums, cur):
            if len(t_nums) <= 0:
                res.append(cur)
            for i, n in enumerate(t_nums):
                back(t_nums[:i] + t_nums[i + 1:], [n] + cur)

        back(nums, [])
        return res


# @lc code=end


print(Solution().permute([1, 2, 3]))
