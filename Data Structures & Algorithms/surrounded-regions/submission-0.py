class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if (m <= r or r < 0 or n <= c or c < 0 or
            board[r][c] != 'O'):
                return
            board[r][c] = '#'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 遍历左边界和右边界（固定列，遍历行）
        for r in range(m):
            if board[r][0] == 'O':
                # 触发搜索
                dfs(r, 0)
            if board[r][n - 1] == 'O':
                # 触发搜索
                dfs(r, n - 1)

        # 遍历上边界和下边界（固定行，遍历列）
        for c in range(n):
            if board[0][c] == 'O':
                # 触发搜索
                dfs(0, c)
            if board[m - 1][c] == 'O':
                # 触发搜索
                dfs(m - 1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'