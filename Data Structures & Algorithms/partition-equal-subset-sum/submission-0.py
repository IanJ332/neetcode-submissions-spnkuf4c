class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # 1. 如果总和是奇数，直接返回 False ❌
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # 2. dp 数组长度为 target + 1 📏
        dp = [False] * (target + 1)
        dp[0] = True  # 凑出 0 总是可行的 🏁

        # 3. 遍历每个数字 🔄
        for num in nums:
            # 从 target 倒序遍历到 num ⏳
            for w in range(target, num - 1, -1):
                if dp[w - num]:
                    dp[w] = True
                    
        return dp[target]