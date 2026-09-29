class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 任意两个区间 $A$ 和 $B$ 要发生相交（重叠），
        # 必须同时满足两个条件：
        #     🔹 A 的右端点 B 的左端点（A 不能完全在 B 的左边）
        #     🔹 B 的右端点 A 的左端点（B 不能完全在 A 的左边）
        res = []
        i = 0
        n = len(intervals)

        # 阶段 1：把所有在 newInterval 左侧且完全不重叠的区间加入结果 ⬅️
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 阶段 2：合并所有与 newInterval 有重叠的区间 🔀
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        # 阶段 3：把右侧剩余的区间全部加入结果 ➡️
        while i < n:
            res.append(intervals[i])
            i += 1
        return res