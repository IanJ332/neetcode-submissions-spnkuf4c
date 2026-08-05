class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        res = 0
        visited = set()
        def dfs(r, c):
            if (
               r < 0 or r >= row or
               c < 0 or c >= col or
               (r, c) in visited or
               grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
            return area
        
        for r in range(row):
            for c in range(col):
                res = max(dfs(r, c), res)
        return res