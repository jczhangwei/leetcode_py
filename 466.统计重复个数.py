#
# @lc app=leetcode.cn id=466 lang=python3
#
# [466] 统计重复个数
#
# https://leetcode-cn.com/problems/count-the-repetitions/description/
#
# algorithms
# Hard (37.98%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 27K
# Testcase Example:  '"acb"\n4\n"ab"\n2'
#
# 由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。
#
# 如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec”
# 获得，但不能从 “acbbe” 获得。
#
# 现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 10^6 和 1 ≤ n2 ≤ 10^6。现在考虑字符串
# S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。
#
# 请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。
#
#
#
# 示例：
#
# 输入：
# s1 ="acb",n1 = 4
# s2 ="ab",n2 = 2
#
# 返回：
# 2
#
#
#
from typing import *

# @lc code=start


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        store = dict()
        index = 0
        num_s1 = 0
        num_s2 = 0
        while(True):
            num_s1 += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index >= len(s2):
                        index = 0
                        num_s2 += 1

            if num_s1 == n1:
                return int(num_s2 // n2)

            if index in store:
                pre_num_s1, pre_num_s2 = store[index]
                pre = (pre_num_s1, pre_num_s2)
                inloop = (num_s1 - pre_num_s1, num_s2 - pre_num_s2)
                break
            else:
                store[index] = (num_s1, num_s2)

        times = pre[1] + (n1 - pre[0])//inloop[0] * inloop[1]
        rem_s1_num = (n1 - pre[0]) % inloop[0]

        for j in range(rem_s1_num):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index >= len(s2):
                        index = 0
                        times += 1

        return int(times // n2)

        # @lc code=end


print(Solution().getMaxRepetitions("acb", 1, "acb", 1))
print(Solution().getMaxRepetitions("aaa",20,"aaaaa",1))
