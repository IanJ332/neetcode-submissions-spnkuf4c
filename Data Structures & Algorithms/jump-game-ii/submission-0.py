class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            curr_step = dp[i] + 1
            j = i + 1
            while j <= len(nums) - 1 and j <= (nums[i] + i):
                dp[j] = min(dp[j], curr_step)
                j += 1

        return dp[-1]