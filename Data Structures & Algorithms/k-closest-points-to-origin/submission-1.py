class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 策略 A（全建堆）：把所有 N 个点及其距离全压入小顶堆，然后连续 pop K 次
        my_heap = []
        
        for i in range(len(points)):
            p = points[i]
            x, y = p[0], p[1]
            dist = x**2 + y**2
            heapq.heappush(my_heap, (dist, p))
        res = []

        for _ in range(k):
            dist, point = heapq.heappop(my_heap)
            res.append(point)
        return res