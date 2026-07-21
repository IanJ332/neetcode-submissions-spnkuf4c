class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 思路 A
        # # 1. 🌿 情况一：如果堆还没满（少于 k 个），不管三七二十一，直接加进去！
        # if len(self.heap) < self.k:
        #     heapq.heappush(self.heap, val)
            
        # # 2. 👑 情况二：堆已经满了，只有当 val 比堆顶大时，才踢掉堆顶换新的
        # elif val > self.heap[0]:
        #     heapq.heappop(self.heap)
        #     heapq.heappush(self.heap, val)
            
        # # 3. 🎯 无论怎样，当前的堆顶就是第 k 大的数
        # return self.heap[0]

        # # 思路 B（先加再弹法）
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
