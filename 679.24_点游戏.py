#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
# https://leetcode-cn.com/problems/24-game/description/
#
# algorithms
# Hard (44.08%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    14.1K
# Total Submissions: 26.9K
# Testcase Example:  '[4,1,8,7]'
#
# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
#
# 示例 1:
#
# 输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
#
#
# 示例 2:
#
# 输入: [1, 2, 1, 2]
# 输出: False
#
#
# 注意:
#
#
# 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
# 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
# 是不允许的。
# 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
#
#
#

from typing import *
# @lc code=start

TARGET = 24
ACCURACY = 1e-6

ADD = 0
MUL = 1
SUB = 2
DIV = 3


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.judge(list(nums))

    def judge(self, nums: List[int]) -> bool:
        l = len(nums)
        if l <= 0:
            return False

        if l == 1 and abs(nums[0] - TARGET) <= ACCURACY:
            return True

        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i == j:
                    continue

                new_nums = []
                for k, v in enumerate(nums):
                    if k != i and k != j:
                        new_nums.append(v)

                for fu in range(0, 4):
                    if fu < 2 and i > j:
                        continue

                    if fu == ADD:
                        new_nums.append(a + b)

                    if fu == MUL:
                        new_nums.append(a * b)

                    if fu == SUB:
                        new_nums.append(a - b)

                    if fu == DIV:
                        if abs(b) < ACCURACY:
                            continue
                        new_nums.append(a / b)

                    if self.judge(new_nums):
                        return True

                    new_nums.pop()

        return False


                    # @lc code=end


print(Solution().judgePoint24([4,1,8,7]));