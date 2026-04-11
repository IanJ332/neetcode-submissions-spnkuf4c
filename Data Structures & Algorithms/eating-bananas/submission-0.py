class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r 
        
        while l <= r:
            mid = (l + r) // 2
    
            total_time = 0
            for p in piles:
                total_time += (p + mid - 1) // mid
            
            if total_time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return res