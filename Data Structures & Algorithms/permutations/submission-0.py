class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i, path):
            if len(path) == len(nums):
                res.append(path[:])

            for j in range(len(nums)):
                if nums[j] not in path:
                    dfs(j + 1, path +[nums[j]])
                else:
                    continue
        dfs(0, [])
        return res