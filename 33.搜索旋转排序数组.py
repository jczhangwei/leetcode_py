#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (39.21%)
# Likes:    1038
# Dislikes: 0
# Total Accepted:    185K
# Total Submissions: 470.4K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 给你一个升序排列的整数数组 nums ，和一个整数 target 。
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
#
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#
# 示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1
# -10^4
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4
#
#
#
from typing import *
# @lc code=start

# 被旋转过的话，前半部分的所有元素一定都比后半部分大


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l <= 0:
            return -1

        if l <= 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        s = 0
        e = l - 1
        while s <= e:
            mid = (e + s)//2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:
                if target >= nums[0] and target < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                if target > nums[mid] and target <= nums[l - 1]:
                    s = mid + 1
                else:
                    e = mid - 1

        return -1

        # @lc code=end

print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 4))
print(Solution().search([4,5,6,7,0,1,2], 5))
print(Solution().search([4,5,6,7,0,1,2], 1))