class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. 🔀 按照起点升序排序
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # 2. 📥 如果结果为空，或者当前区间与上一个区间不重叠
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 3. 🔀 发生重叠，只需扩展右边界
                # 因为我们一开始已经做了 intervals.sort(key=lambda x: x[0])（按起点升序排序）
                # 所以后面遇到的每个区间，它的起点一定 >= 前面区间的起点
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged