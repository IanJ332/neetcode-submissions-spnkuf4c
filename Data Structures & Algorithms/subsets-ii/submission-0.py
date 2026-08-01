class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, path):
            res.append(path[:])

            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j - 1]:
                    continue
                
                dfs(j + 1, path +[nums[j]])


        
        dfs(0, [])
        return res