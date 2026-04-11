class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            sub_num = nums[nums.index(num) + 1:]
            if target - num in sub_num:
                return [nums.index(num), 1 + nums.index(num) + sub_num.index(target - num)]
        return False
            