#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (38.89%)
# Likes:    3351
# Dislikes: 0
# Total Accepted:    279.1K
# Total Submissions: 716.8K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
#
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
# 示例 3：
#
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
#
# 示例 4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
#
# 示例 5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
from typing import *
# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findk(nums1, nums2, k):

            start_a = 0
            start_b = 0
            while True:
                if start_a == len(nums1):
                    return nums2[start_b + k - 1]
                if start_b == len(nums2):
                    return nums1[start_a + k - 1]

                if k == 1:
                    return min(nums1[start_a], nums2[start_b])

                half = k//2
                ai = min(half + start_a, len(nums1)) - 1
                bi = min(half + start_b, len(nums2)) - 1

                if nums1[ai] <= nums2[bi]:
                    k -= ai - start_a + 1
                    start_a = ai + 1
                else:
                    k -= bi - start_b + 1
                    start_b = bi + 1

        tl = len(nums1) + len(nums2)
        if tl % 2 == 0:
            return (findk(nums1, nums2, tl // 2) + findk(nums1, nums2, tl // 2 + 1)) / 2
        else :
            return findk(nums1, nums2, tl // 2 + 1)
            
            # @lc code=end


print(Solution().findMedianSortedArrays([2,3,4,5,6],[1]))
print(Solution().findMedianSortedArrays([1,3], nums2 = [2]))