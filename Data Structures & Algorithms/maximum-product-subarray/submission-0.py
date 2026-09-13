class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        dp = [(0,0)] * (len(nums))
        dp[0] = (nums[0], nums[0])
        for i in range(1, len(nums)):
            prev_max, prev_min = dp[i - 1]
            new_max = prev_max * nums[i]
            new_min = prev_min * nums[i]
            
            dp[i] = (max(nums[i], new_max, new_min), min(nums[i], new_max, new_min))
            res = max(res, dp[i][0])
        return res
            
