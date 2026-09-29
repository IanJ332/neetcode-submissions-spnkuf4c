class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 阶段 1：把所有在 newInterval 左侧且完全不重叠的区间加入结果 ⬅️
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 阶段 2：合并所有与 newInterval 有重叠的区间 🔀
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 阶段 3：把右侧剩余的区间全部加入结果 ➡️
        while i < n:
            res.append(intervals[i])
            i += 1

        return res