class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        nums = Counter(tasks)
        max_heap = [-x for x in nums.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            temp = []
            for _ in range(n+1):
            # 模拟一个大小为 n + 1 的时间窗口
                if max_heap:
                    count = heapq.heappop(max_heap)
                    if count + 1 < 0:
                        temp.append(count + 1)
                    time += 1

                else:
                    if temp:
                        time += 1
                    else:
                        break
            # 缩进对齐 for _ in range(n + 1)：在整个窗口结束后，再统一放回大顶堆
            for count in temp:
                heapq.heappush(max_heap, count)
        return time