#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
# https://leetcode-cn.com/problems/design-hashmap/description/
#
# algorithms
# Easy (57.71%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    16.3K
# Total Submissions: 28.1K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get", "remove", "get"]\n' +'[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希映射
#
# 具体地说，你的设计应该包含以下的功能
#
#
# put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
# get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
# remove(key)：如果映射中存在这个键，删除这个数值对。
#
#
#
# 示例：
#
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);
# hashMap.get(1);            // 返回 1
# hashMap.get(3);            // 返回 -1 (未找到)
# hashMap.put(2, 1);         // 更新已有的值
# hashMap.get(2);            // 返回 1
# hashMap.remove(2);         // 删除键为2的数据
# hashMap.get(2);            // 返回 -1 (未找到)
#
#
#
# 注意：
#
#
# 所有的值都在 [0, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希库。
#
#
#
from typing import *

# @lc code=start


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.storage = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.storage[self._hash(key)].add(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        node = self.storage[self._hash(key)].get(key)
        if node:
            return node.value

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.storage[self._hash(key)].remove(key)


class Node():
    def __init__(self, key, value, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next


class Bucket:

    def __init__(self) -> None:
        self.head = None
        pass

    def get(self, key):
        head = self.head
        while head:
            if head.key == key:
                return head
            head = head.next

    def add(self, key, value):
        head = self.get(key)
        if head:
            head.value = value
        else:
            self.head = Node(key, value, self.head)

    def contains(self, key):
        head = self.head
        while head:
            if head.key == key:
                return True
            head = head.next

        return False

    def remove(self, key):
        head = self.head
        pre = None
        while head:
            if head.key == key:
                if pre:
                    pre.next = head.next
                else:
                    self.head = head.next
                return
            pre = head
            head = head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end


s = MyHashMap()
s.put(3, "v3")
print("print(3: " + str(s.get(3)))
print("print(2: " + str(s.get(2)))
s.remove(3)
print("print(3: " + str(s.get(3)))
s.put(2, "v2")
print("print(2: " + str(s.get(2)))
s.put(2, "v22")
print("print(2: " + str(s.get(2)))
s.put(771, "v771")
print("print(2: " + str(s.get(2)))
print("print(771: " + str(s.get(771)))
s.remove(771)
print("print(2: " + str(s.get(2)))
print("print(771: " + str(s.get(771)))
s.remove(771)
