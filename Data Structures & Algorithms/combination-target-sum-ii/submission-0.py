class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start, path):
            if sum(path) == target:
                res.append(path[:])
                return
            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                if sum(path) + candidates[j] > target:
                    break
                dfs(j + 1, path + [candidates[j]])
        dfs(0, [])
        return res