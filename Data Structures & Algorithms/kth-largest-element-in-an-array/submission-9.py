class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. 🧱 将原数组原地转换为小顶堆 (Min-Heap)
        my_heap = nums
        heapq.heapify(my_heap)

        # 2. ✂️ 不断弹出最小值，直到堆里只剩下最大的 k 个元素
        while len(my_heap) != k:
            heapq.heappop(my_heap)
        
        # 3. 🛡️ 直接返回[0]因为这个肯定是当前 heappop之后最小的
        # 也就是 Kth Largest Element in an Array
        return my_heap[0]