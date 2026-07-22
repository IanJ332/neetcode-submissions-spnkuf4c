class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 策略 B（维持大小为 K 的堆）：只维持一个大小为 K 的大顶堆（用负数），遍历所有点时动态替换。
        my_heap = []
        heapq.heapify(my_heap)
        for i in range(len(points)):
            p = points[i]
            x, y = p[0], p[1]
            dist = -abs(x**2 + y**2)

            heapq.heappush(my_heap, (dist, p))

            while len(my_heap) > k:
                heapq.heappop(my_heap)
        res = []
        for neg_dist, p in my_heap:
            res.append(p)
        return res

