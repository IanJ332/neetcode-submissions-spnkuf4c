class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = nums
        heapq.heapify(my_heap)

        while len(my_heap) != k:
            heapq.heappop(my_heap)
        
        return my_heap[0]
