class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计频率
        count = Counter(nums)
        
        # 2. 创建频率桶
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # 3. 将数字送入对应的频率桶
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 4. 从后往前倒出前 k 个元素
        res = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res