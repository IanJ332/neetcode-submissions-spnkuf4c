class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        nums = Counter(tasks)
        max_heap = [-x for x in nums.values()]
        heapq.heapify(max_heap)

        f = heapq.heappop(max_heap)
        m = 1
        while max_heap and heapq.heappop(max_heap) == f :
            m += 1
        f = abs(f)
        return max(((f - 1) * (n + 1) + m), len(tasks))