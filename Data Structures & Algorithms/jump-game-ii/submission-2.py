class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        
        for i in range(len(nums)):
            curr_step = dp[i] + 1
            j = i + 1

            while j <= (nums[i] + i) and j <= len(nums) - 1:
                dp[j] = min(curr_step, dp[j])
                j += 1
        return dp[-1]