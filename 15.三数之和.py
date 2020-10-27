#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (29.82%)
# Likes:    2704
# Dislikes: 0
# Total Accepted:    353K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for k, n in enumerate(nums):
            if k > 0 and nums[k - 1] == n:
                continue
            if n > 0:
                break
            
            i = k + 1
            j = l - 1

            while i < j :
                r = n + nums[i] + nums[j]
                if r == 0:
                    res.append([n, nums[i], nums[j]])
                    
                if r <= 0:
                    i = i + 1
                    while nums[i - 1] == nums[i] and i < j:
                        i = i + 1

                if r >= 0:
                    j = j - 1
                    while nums[j] == nums[j + 1] and i < j:
                        j = j - 1


        return res

# @lc code=end

