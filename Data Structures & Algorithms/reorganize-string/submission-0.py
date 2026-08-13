import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = Counter(s)
        
        # 1. 检查可行性：最高频次不能超过 (n + 1) // 2
        if max(count.values()) > (n + 1) // 2:
            return ""
        
        # 2. 构建大顶堆：存入 (-频次, 字符)
        # 比如 ('a', 3) 会变成 (-3, 'a')
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        res = []
        
        # 3. 循环处理：只要堆里至少有 2 个不同字符，就成对取出
        while len(max_heap) >= 2:
            # 弹出当前频次最高和次高的两个字符
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            
            # 拼接到结果中
            res.append(char1)
            res.append(char2)
            
            # 频次 +1（因为是负数，加 1 相当于用掉一次，剩余频次减少）
            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))
                
        # 4. 处理残余：如果堆里还剩最后一个字符
        if max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)
            
        return "".join(res)