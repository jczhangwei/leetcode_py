#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (48.78%)
# Likes:    670
# Dislikes: 0
# Total Accepted:    222.5K
# Total Submissions: 455.9K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
# 说明：
#
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
# 示例：
#
#
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出：[1,2,2,3,5,6]
#
#
#
# 提示：
#
#
# -10^9
# nums1.length == m + n
# nums2.length == n
#
#
#
from typing import *
# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 or n >= 0:
            if n >= 0 :
                if m >= 0:
                    if nums1[m] < nums2[n]:
                        nums1[p] = nums2[n]
                        n -= 1
                    else:
                        nums1[p] = nums1[m]
                        m -= 1
                else:
                    nums1[p] = nums2[n]
                    n -= 1
            else:
                nums1[p] = nums1[m]
                m -= 1
            p -= 1

        pass
# @lc code=end


Solution().merge([2, 0], 1, [1], 1)
Solution().merge([0], 0, [2], 1)
Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
