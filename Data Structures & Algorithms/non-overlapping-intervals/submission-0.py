class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 1. 🔀 优先保留结束最早的区间：按结束时间升序排序
        intervals.sort(key=lambda x: x[1])
        
        counter = 0
        prev_end = intervals[0][1]

        # 2. 🚶 从第 2 个区间开始逐个检查
        for interval in intervals[1:]:
            # 没有冲突：保留该区间，更新最新的结束时间 🕒
            if interval[0] >= prev_end:
                prev_end = interval[1]
            # 发生冲突：舍弃当前区间，计数器累加 ➕
            else:
                counter += 1

        return counter