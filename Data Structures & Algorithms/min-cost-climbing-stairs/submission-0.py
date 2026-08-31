class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        if len(cost) <= 1:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])

        prev1, prev2 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev1, prev2 = prev2, curr
        
        return min(prev1, prev2)