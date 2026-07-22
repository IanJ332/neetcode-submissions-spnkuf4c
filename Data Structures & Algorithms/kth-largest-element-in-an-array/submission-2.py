class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = nums
        heapq.heapify(my_heap)
        
        while len(my_heap) != k:
            heapq.heappop(my_heap)
        
        # negative = -abs(my_heap)
        heap = [-x for x in my_heap]
        res = -heap[0]
        return res
