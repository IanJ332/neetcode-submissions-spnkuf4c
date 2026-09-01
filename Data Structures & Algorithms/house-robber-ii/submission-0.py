class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. 单独处理只有 1 间房的特殊情况
        if len(nums) == 1:
            return nums[0]

        # 2. 线性打家劫舍辅助函数
        def rob_linear(start: int, end: int) -> int:
            if end - start == 1:
                return nums[start]
            
            prev2 = nums[start]
            prev1 = max(nums[start], nums[start + 1])

            for i in range(start + 2, end):
                money = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = money

            return prev1
        
        # 3. 分别计算两种方案取最大值
        return max(rob_linear(0, len(nums) - 1), rob_linear(1, len(nums)))