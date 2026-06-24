class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # 为了防止最后剩下两个元素时死循环，用 <=
        while left <= right:
            mid = (left + right) // 2  # 1. 补上缺失的 mid 计算
            
            if nums[mid] == target:
                return mid
            
            # 2. 判断 mid 是落在【左大区】还是【右小区】
            if nums[mid] >= nums[left]:  # mid 落在左大区，说明左边是干净的升序区间
                # 3. 铁证如山：target 必须被死死锁在左边区间内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1     # 往左边找
                else:
                    left = mid + 1      # 自动去右边了！
                    
            else:                        # mid 落在右小区，说明右边是干净的升序区间
                # 3. 铁证如山：target 必须被死死锁在右边区间内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1      # 往右边找
                else:
                    right = mid - 1     # 自动去左边了！
                    
        return -1  # 找不到返回 -1