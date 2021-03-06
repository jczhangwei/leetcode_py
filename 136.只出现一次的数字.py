#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (69.69%)
# Likes:    1481
# Dislikes: 0
# Total Accepted:    268.4K
# Total Submissions: 384.3K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#

# @lc code=start
from cmath import sin


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for k, v in enumerate(nums):
            if v in s:
                s.discard(v)
            else:
                s.add(v)
        for k, v in enumerate(s):
            return v

# 答案是使用位运算。对于这道题，可使用异或运算 ⊕。异或运算有以下三个性质。
# 任何数和 00 做异或运算，结果仍然是原来的数，即 a⊕0=a。
# 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
# 异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for k, v in enumerate(nums):
            single ^= v

        return single 
# @lc code=end

