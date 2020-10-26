#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (52.79%)
# Likes:    1773
# Dislikes: 0
# Total Accepted:    159.8K
# Total Submissions: 302.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 0
# 0
#
#
#
from typing import *
# @lc code=start

# 暴力


class Solution1:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        water = 0
        for i, hc in enumerate(height):
            right = 0
            for j in range(i + 1, l):
                if height[j] >= right:
                    right = height[j]
            left = 0
            for j in range(0, i):
                if height[j] >= left:
                    left = height[j]

            water += max(min(left, right) - hc, 0)

        return water

# 动态规划


class Solution2:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l <= 2:
            return 0
        water = 0
        max_left = {}
        max_left[0] = height[0]
        for i in range(1, l):
            max_left[i] = max(max_left[i - 1], height[i])

        max_right = {}
        max_right[l - 1] = height[l - 1]
        for i in range(l - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        for i in range(l):
            water += max(0, min(max_left[i], max_right[i]) - height[i])

        return water

# 栈


class Solution3:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l <= 2:
            return 0
        water = 0
        stack = []
        for i in range(l):
            cur = height[i]
            while len(stack) > 0 and cur >= height[stack[-1]]:
                pre = stack.pop()
                if len(stack) <= 0:
                    break
                dis = i - stack[-1] - 1
                water += dis * (min(height[stack[-1]], cur) - height[pre])

            stack.append(i)

        return water


# 双指针
class Solution4:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l <= 2:
            return 0
        water = 0

        left_max = 0
        right_max = 0
        left = 0
        right = l - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    water += left_max - height[left]
                left_max = max(left_max, height[left])
                left += 1
            else:
                if height[right] < right_max:
                    water += right_max - height[right]
                right_max = max(right_max, height[right])
                right -= 1

        return water
# @lc code=end


case1 = [4, 2, 0, 3, 2, 5]
print(Solution1().trap(case1))
print(Solution2().trap(case1))
print(Solution2().trap([]))
print(Solution3().trap(case1))
print(Solution3().trap([]))
print(Solution4().trap(case1))
print(Solution4().trap([]))
