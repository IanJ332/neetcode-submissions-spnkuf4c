class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target =  sum(nums) // 2

        if sum(nums) % 2 != 0:
            return False
        
        dp = [False] * (target + 1)
        dp[0] =  True

        for num in nums:
            for w in range(target, num - 1, -1):
                if dp[w - num]:
                    dp[w] = True

        return dp[target]