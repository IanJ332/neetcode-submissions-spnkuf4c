class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. 🧱 将原数组原地转换为小顶堆 (Min-Heap)
        my_heap = nums
        heapq.heapify(my_heap)

        # 2. ✂️ 不断弹出最小值，直到堆里只剩下最大的 k 个元素
        while len(my_heap) != k:
            heapq.heappop(my_heap)

        # 3. 🛡️ 用取负数的方式取出堆顶元素，成功避开了 abs() 对负数的错误转换
        heap = [-x for x in my_heap]
        res = -heap[0]
        return res