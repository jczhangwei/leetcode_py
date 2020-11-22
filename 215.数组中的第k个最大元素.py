#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.41%)
# Likes:    793
# Dislikes: 0
# Total Accepted:    224.9K
# Total Submissions: 348.7K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#

#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#
import random
from typing import *
# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def qsort(start, end, c):
            if end - start <= 1:
                return nums

            m = random.randint(start, end - 1)
            nums[m], nums[start] = nums[start], nums[m]
            mid = nums[start]

            i = start
            for j in range(i + 1, end):
                if nums[j] >= mid:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1

            nums[i], nums[start] = nums[start], nums[i]
            f_c = i - start
            if f_c >= c:
                return qsort(start, i, c)
            else:
                return qsort(i, end, c - f_c)

        r = qsort(0, len(nums), k)

        return r[k - 1]
# @lc code=end


print(Solution().findKthLargest([-1, 2, 0], 3))
print(Solution().findKthLargest([99, 99], k=1))
print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2))
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
