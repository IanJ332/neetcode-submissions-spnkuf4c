class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0 # 统计新鲜橘子数量 🍊
        time = 0

        # 1. 初始化：收集所有腐烂橘子起点，并统计新鲜橘子数量
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # 如果一开始就没有新鲜橘子，直接返回 0
        if fresh == 0:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # 2. 按层 BFS（每一层代表 1 分钟）
        while q and fresh > 0: # 只要还有新鲜橘子并且队列不为空就继续
            length = len(q)
            
            for i in range(length):
                r, c = q.popleft() # 👈 在内层循环弹出元素

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < row and 
                        0 <= nc < col and 
                        grid[nr][nc] == 1):
                        
                        grid[nr][nc] = 2 # ☣️ 标记为腐烂
                        fresh -= 1       # 🍊 新鲜橘子减少 1
                        q.append((nr, nc))
            
            time += 1 # 这一层全部扩散完，时间 +1

        # 3. 如果还有新鲜橘子无法被感染，返回 -1，否则返回耗时
        return time if fresh == 0 else -1