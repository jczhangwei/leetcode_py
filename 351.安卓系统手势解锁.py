#
# @lc app=leetcode.cn id=351 lang=python3
#
# [351] 安卓系统手势解锁
#
# https://leetcode-cn.com/problems/android-unlock-patterns/description/
#
# algorithms
# Medium (57.25%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 6.1K
# Testcase Example:  '1\n1'
#
# 我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。
#
# 给你两个整数，分别为 ​​m 和 n，其中 1 ≤ m ≤ n ≤ 9，那么请你统计一下有多少种解锁手势，是至少需要经过 m 个点，但是最多经过不超过 n
# 个点的。
#
#
#
# 先来了解下什么是一个有效的安卓解锁手势:
#
#
# 每一个解锁手势必须至少经过 m 个点、最多经过 n 个点。
# 解锁手势里不能设置经过重复的点。
# 假如手势中有两个点是顺序经过的，那么这两个点的手势轨迹之间是绝对不能跨过任何未被经过的点。
# 经过点的顺序不同则表示为不同的解锁手势。
#
#
#
#
#
#
#
#
# 解释:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
#
# 无效手势：4 - 1 - 3 - 6
# 连接点 1 和点 3 时经过了未被连接过的 2 号点。
#
# 无效手势：4 - 1 - 9 - 2
# 连接点 1 和点 9 时经过了未被连接过的 5 号点。
#
# 有效手势：2 - 4 - 1 - 3 - 6
# 连接点 1 和点 3 是有效的，因为虽然它经过了点 2 ，但是点 2 在该手势中之前已经被连过了。
#
# 有效手势：6 - 5 - 4 - 1 - 9 - 2
# 连接点 1 和点 9 是有效的，因为虽然它经过了按键 5 ，但是点 5 在该手势中之前已经被连过了。
#
#
#
# 示例:
#
# 输入: m = 1，n = 1
# 输出: 9
#
#
#
from types import coroutine
from typing import *
# @lc code=start


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        if n <= 0:
            return 0

        def valid(cur_nums: List[int], new_num) -> bool:
            if len(cur_nums) <= 0:
                return True
            if cur_nums.count(new_num) > 0:
                return False
            last_num = cur_nums[-1]
            sub = abs(last_num - new_num)
            if (last_num + new_num) % 2 == 1:
                return True
            mid = (last_num + new_num) / 2
            if mid == 5:
                return cur_nums.count(mid) > 0

            if (last_num - 1) % 3 != (new_num - 1) % 3 and (last_num - 1)//3 != (new_num - 1)//3:
                return True

            return cur_nums.count(mid) > 0

        def count(cur_nums):
            num = 0

            if len(cur_nums) >= m:
                num += 1

            if len(cur_nums) >= n:
                return num

            for i in range(1, 10):
                if valid(cur_nums, i):
                    cur_nums.append(i)
                    num += count(cur_nums)
                    cur_nums.pop()

            return num

        return count([])

        # @lc code=end


print(Solution().numberOfPatterns(1, 2))
print(Solution().numberOfPatterns(1, 1))
print(Solution().numberOfPatterns(0, 0))
