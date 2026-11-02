class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curr_end = 0
        max_reach = 0

        # 遍历到倒数第二个元素即可
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            
            # 当走到当前步数的边界时，强制跳跃并更新边界
            if i == curr_end:
                jump += 1
                curr_end = max_reach
                
        return jump