# 253. 会议室 II
# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间
# [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑
# 充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

# 示例 1:

# 输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2
# 示例 2:

# 输入: [[7,10],[2,4]]
# 输出: 1
# 通过次数16,301提交次数34,921


# 最后留在队列里的都是没有别的会议和它共用一个会议室的会议，消除了所有重复，
# 所以最后堆的大小就是答案

from typing import *
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        store = []
        heapq.heapify(store)
        for i, interval in enumerate(intervals):
            if len(store) > 0 and store[0] <= interval[0]:
                heapq.heappop(store)
            heapq.heappush(store, interval[1]) 
        

        return len(store)

print(Solution().minMeetingRooms([[13,15],[1,13]]))
print(Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(Solution().minMeetingRooms([[7,10],[2,4]]))