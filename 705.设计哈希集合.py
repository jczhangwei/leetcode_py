#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#
# https://leetcode-cn.com/problems/design-hashset/description/
#
# algorithms
# Easy (57.29%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 31.7K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +  '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希集合
#
# 具体地说，你的设计应该包含以下的功能
#
#
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
#
#
#
# 示例:
#
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // 返回 true
# hashSet.contains(3);    // 返回 false (未找到)
# hashSet.add(2);          
# hashSet.contains(2);    // 返回 true
# hashSet.remove(2);          
# hashSet.contains(2);    // 返回  false (已经被删除)
#
#
#
# 注意：
#
#
# 所有的值都在 [0, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。
#
#
#
from typing import *
# @lc code=start


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.storage = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        self.storage[self._hash(key)].add(key)

    def remove(self, key: int) -> None:
        self.storage[self._hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.storage[self._hash(key)].contains(key)


class Node():
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class Bucket:

    def __init__(self) -> None:
        self.head = None
        pass

    def add(self, key):
        last_head = Node
        if not self.contains(key):
            self.head = Node(key, self.head)

    def contains(self, key):
        head = self.head
        while head:
            if head.value == key:
                return True
            head = head.next

        return False

    def remove(self, key):
        head = self.head
        pre = None
        while head:
            if head.value == key:
                if pre:
                    pre.next = head.next
                else:
                    self.head = head.next
                return
            pre = head
            head = head.next

    # Your MyHashSet object will be instantiated and called as such:
    # obj = MyHashSet()
    # obj.add(key)
    # obj.remove(key)
    # param_3 = obj.contains(key)
    # @lc code=end


s = MyHashSet()
s.add(3)
print("print(3: " + str(s.contains(3)))
print("print(2: " + str(s.contains(2)))
s.remove(3)
print("print(3: " + str(s.contains(3)))
s.add(2)
s.add(771)
print("print(2: " + str(s.contains(2)))
print("print(771: " + str(s.contains(771)))
s.remove(771)
print("print(2: " + str(s.contains(2)))
print("print(771: " + str(s.contains(771)))
s.remove(771)
