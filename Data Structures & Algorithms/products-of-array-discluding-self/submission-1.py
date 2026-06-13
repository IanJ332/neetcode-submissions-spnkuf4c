class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_products = [1] * len(nums)
        postfix_products = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_products[i] = prefix_products[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix_products[i] = nums[i + 1] * postfix_products[i + 1]
        
        for i in range(len(prefix_products)):
            res.append(prefix_products[i] * postfix_products[i])
        return res
