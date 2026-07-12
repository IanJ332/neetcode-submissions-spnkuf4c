class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]        # 🐢 乌龟每次走 1 步
            fast = nums[nums[fast]]  # 🐇 兔子每次走 2 步

        slow = nums[0]

        # 1. 乌龟回到起点，兔子先补上一步
        slow = nums[0]
        fast = nums[fast]  # 🐇 兔子先往前走一步，补齐第一阶段起跑时的差距

        # 2. 两人同时每次走 1 步，直到相遇
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow