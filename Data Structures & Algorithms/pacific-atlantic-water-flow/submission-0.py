class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row, col = len(heights), len(heights[0])
        directions = ([1,0],[-1,0],[0,1],[0,-1])
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean_set):
            ocean_set.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if(
                    0 <= nr < row and
                    0 <= nc < col and
                    (nr, nc) not in ocean_set and
                    heights[nr][nc] >= heights[r][c]
                ):
                    
                    dfs(nr, nc, ocean_set)
        for r in range(row):
            dfs(r, 0, pacific)
            dfs(r, col - 1, atlantic)
        for c in range(col):
            dfs(0, c, pacific)
            dfs(row - 1, c, atlantic)
        return list(pacific & atlantic)
