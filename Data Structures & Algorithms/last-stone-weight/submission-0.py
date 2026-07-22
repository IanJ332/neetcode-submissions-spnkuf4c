class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated = [-x for x in stones]
        my_heap = negated
        heapq.heapify(my_heap)

        while len(my_heap) > 1:
            large = abs(heapq.heappop(my_heap))
            small = abs(heapq.heappop(my_heap))

            if large - small != 0:
                heapq.heappush(my_heap, -abs((large - small)))
        if len(my_heap) == 0:
            return 0
        return abs(heapq.heappop(my_heap))