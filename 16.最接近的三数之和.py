#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (43.94%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    99K
# Total Submissions: 225.2K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        if l < 3:
            return
        res = sys.maxsize
        for k, n in enumerate(nums):
            if k > 0 and n == nums[k - 1]:
                continue
            i = k + 1
            j = l - 1
            while i < j:
                a = n + nums[i] + nums[j]
                if abs(target - a) < abs(target - res):
                    res = a
                if a > target and i < j:
                    j = j - 1
                    while nums[j] == nums[j + 1] and i < j:
                        j = j - 1
                if a < target and i < j:
                    i = i + 1
                    while nums[i] == nums[i - 1] and i < j:
                        i = i + 1
                if a == target:
                    return a
        return res
# @lc code=end

