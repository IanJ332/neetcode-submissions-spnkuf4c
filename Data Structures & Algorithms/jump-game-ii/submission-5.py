class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curr_end = 0
        max_reach = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == curr_end:
                curr_end = max_reach
                jump += 1
                
        return jump