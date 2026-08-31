class Solution:
    def rob(self, nums: List[int]) -> int:
        # 如果小于等于2就直接输出两个里面的最大值
        # 如果是3，就看中间的值是否大于两边的和
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # 如果偷第i个房间，那么
        # 收益1 = dp[i-2] + nums[i]

        # 如果不偷就是
        # 收益2 = dp[i-1]

        # 带到下面的一个应该就是max(收益1，收益2)

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, money

        return money
        
