import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # 1. 初始化二分查找的左右边界
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # 2. 计算以当前速度 mid 吃完所有香蕉需要耗费的总时间
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            
            # 3. ⚖️ 根据总时间与目标时间 h 的对比，收缩边界
            if total_time <= h:
                # 💡 速度够快，尝试找更小的速度
                right = mid
            else:
                # 💡 速度太慢，必须提升速度
                # 请在这里补全 left 的更新代码：
                # __________________
                left = mid + 1
                
        # 当 left 和 right 相遇时，找到的就是最小速度
        return left