class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()
        
        for t in triplets:
            # 🚫 过滤非法三元组：任何一个位置超过目标上限都不可用
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # 🎯 记录合法三元组中能达成的目标位置
            for i, val in enumerate(t):
                if val == target[i]:
                    found.add(i)
                    
            # ⚡ 可选剪枝：如果 3 个位置都凑齐了，可以提前返回
            if len(found) == 3:
                return True
                
        return len(found) == 3