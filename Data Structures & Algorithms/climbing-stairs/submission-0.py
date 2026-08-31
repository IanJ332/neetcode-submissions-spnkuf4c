class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        last1, last2 = 1, 2
        for i in range(3, n + 1):
            curr = last1 + last2
            last1, last2 = last2, curr
            
        return last2