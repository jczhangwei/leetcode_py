#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (51.02%)
# Likes:    957
# Dislikes: 0
# Total Accepted:    107.9K
# Total Submissions: 211.4K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#
#
from typing import *
# @lc code=start


class Node:
    def __init__(self, key: int = 0, x: int = 0, next: 'Node' = None, prev: 'Node' = None):
        self.key = int(key)
        self.val = int(x)
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.line_head = Node()
        self.line_tail = Node()
        self.line_head.next = self.line_tail
        self.line_tail.prev = self.line_head
        self.store = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.store.get(key)
        if not node:
            return -1
        else:
            if self.line_head.next.next != self.line_tail:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.line_head.next.prev = node
                node.next = self.line_head.next
                node.prev = self.line_head
                self.line_head.next = node
            return node.val

    def put(self, key: int, value: int) -> None:
        node = self.store.get(key)
        if node:
            node.val = value
            if self.line_head.next.next != self.line_tail:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.line_head.next.prev = node
                node.next = self.line_head.next
                node.prev = self.line_head
                self.line_head.next = node
        else:
            if len(self.store) >= self.capacity:
                end = self.line_tail.prev
                end.prev.next = self.line_tail
                self.line_tail.prev = end.prev
                del self.store[end.key]

            cur = Node(key, value)
            cur.next = self.line_head.next
            cur.prev = self.line_head
            cur.next.prev = cur
            self.line_head.next = cur
            self.store[key] = cur

            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)
            # @lc code=end


lru = LRUCache(2)
args = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
for i, v in enumerate(["put","put","get","put","get","put","get","get","get"]):
    getattr(lru, v)(*args[i])