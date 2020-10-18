#
# @lc app=leetcode.cn id=170 lang=python3
#
# [170] 两数之和 III - 数据结构设计
#
# https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (41.34%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 10.7K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# 设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。
# 
# add 操作 -  对内部数据结构增加一个数。
# find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。
# 
# 示例 1:
# 
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# 
# 
# 示例 2:
# 
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false
# 
#

import collections
# @lc code=start

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] = (self.nums.get(number) or 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k, n in self.nums.items():
            m = value - k
            c = self.nums.get(m) or 0
            if c >= 2 or (c >=1 and m !=k):
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

obj = TwoSum()
obj.add(0)
obj.add(3)
obj.add(4)
print(obj.find(7))
print(obj.find(3))
