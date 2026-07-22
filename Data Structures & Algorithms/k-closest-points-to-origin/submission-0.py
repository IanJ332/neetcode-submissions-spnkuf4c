class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
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