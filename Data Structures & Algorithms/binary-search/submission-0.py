class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 定义一个辅助递归函数
        def helper(l, r):
            # 基准情况：如果区间为空，说明找不到了
            if l > r:
                return -1
            
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 去右边找
                return helper(mid + 1, r)
            else:
                # 去左边找
                return helper(l, mid - 1)
        
        return helper(0, len(nums) - 1)