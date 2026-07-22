import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. 全部取负数，构建“大顶堆”效果 🏔️
        my_heap = [-x for x in stones]
        heapq.heapify(my_heap)

        # 2. 只要石头数 >= 2，就不断弹出最大的两块对撞 💥
        while len(my_heap) > 1:
            large = abs(heapq.heappop(my_heap))
            small = abs(heapq.heappop(my_heap))

            if large - small != 0:
                heapq.heappush(my_heap, -(large - small))
        
        # 3. 如果最后全都互相抵消了，返回 0 🛡️
        if not my_heap:  # 或者 len(my_heap) == 0
            return 0
        
        # 4. 否则返回剩下最后一块石头的正数值 🎯
        return abs(heapq.heappop(my_heap))