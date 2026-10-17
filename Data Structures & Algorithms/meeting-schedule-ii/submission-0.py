import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # 1. 🔀 按开始时间升序排序
        intervals.sort(key=lambda x: x.start)

        # 2. 🏔️ 初始化最小堆，记录正在使用的会议室的结束时间
        rooms = []
        heapq.heappush(rooms, intervals[0].end)

        # 3. 🚶 遍历剩下的会议
        for interval in intervals[1:]:
            # 如果当前会议的开始时间 >= 最早结束的会议时间，说明可以复用会议室
            if interval.start >= rooms[0]:
                heapq.heappop(rooms)

            # 无论是否复用，当前会议的结束时间都要入堆
            heapq.heappush(rooms, interval.end)

        # 4. 🏁 堆中的元素个数就是所需的最少会议室数量
        return len(rooms)