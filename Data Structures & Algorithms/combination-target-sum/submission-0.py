class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path):
            if sum(path[:]) > target or i == len(nums):
                return
            elif target == sum(path[:]):
                res.append(path[:])
                return

            dfs(i, path + [nums[i]])
            dfs(i+1, path)
        
        dfs(0, [])
        return res