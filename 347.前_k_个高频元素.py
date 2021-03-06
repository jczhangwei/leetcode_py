#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (61.69%)
# Likes:    547
# Dislikes: 0
# Total Accepted:    111.5K
# Total Submissions: 180.7K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 
# 
# 示例 2:
# 
# 输入: nums = [1], k = 1
# 输出: [1]
# 
# 
# 
# 提示：
# 
# 
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
# 
# 
#
from typing import *
import random
# @lc code=start
# 快速排序法更有意思，必做

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def qsort(items, start, end, m):
            if end - start <= m:
                return start, end
            middle = random.randint(start, end - 1)
            items[start], items[middle] = items[middle], items[start]
            

            middle_value = items[start][1]
            index = start
            for i in range(start + 1, end):
                if items[i][1] >= middle_value:
                    items[index + 1], items[i] = items[i], items[index + 1]
                    index += 1
            
            items[index], items[start] = items[start], items[index]

            up_num = index - start
            if up_num >= m:
                return qsort(items, start, index, m)
            else:
                s, e = qsort(items, index, end, m - up_num)
                return start, e

        store = {}
        for _, v in enumerate(nums):
            store[v] = (store.get(v) or 0) + 1    
        
        items = list(store.items())
        start, end = qsort(items, 0, len(items), k)
        return [x[0] for x in items[start:end]]
        

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for _, v in enumerate(nums):
            store[v] = (store.get(v) or 0) + 1
        
        heap = []
        for i, v in store.items():
            if len(heap) < k:
                heap.append((i, v))
            else: 
                m_v = min(heap, key = lambda x: x[1])
                if m_v[1] < v:
                    heap[heap.index(m_v)] = (i, v)
        
        return [i[0] for _, i in enumerate(heap)]
            

# @lc code=end

print(Solution().topKFrequent([1,1,1, 2,2,3,3,3,3,4,4,4], 3))