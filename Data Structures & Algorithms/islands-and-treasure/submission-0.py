from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()

        # 1. 找到所有宝藏起点，一齐加入队列
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # 2. 多源 BFS 像水波纹一样同步扩散
        while q:
            r, c = q.popleft() # 👈 弹出当前中心点 (r, c)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc # 👈 计算四周邻居 (nr, nc)

                # 检查边界，并且只向未被覆盖的空地 INF 扩散
                if (0 <= nr < row and 
                    0 <= nc < col and 
                    grid[nr][nc] == 2147483647):

                    grid[nr][nc] = grid[r][c] + 1 # 先到的必定是最短距离！
                    q.append((nr, nc))