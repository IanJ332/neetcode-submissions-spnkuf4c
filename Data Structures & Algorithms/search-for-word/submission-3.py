class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visted = set()
        def dfs(r, c, k):
            if k == len(word):
                return True

            if (r < 0 or r >= row or 
               c < 0 or c >= col or 
               board[r][c] != word[k] or
               (r, c) in visted):
                return False
            
            visted.add((r, c))

            if (dfs(r, c - 1, k + 1)or
               dfs(r, c + 1, k + 1)or
               dfs(r - 1, c, k + 1)or
               dfs(r + 1, c, k + 1)):
                return True

            visted.remove((r, c))
            return False
            
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False

