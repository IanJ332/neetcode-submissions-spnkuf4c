class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row, col = len(matrix), len(matrix[0])
        top = 0
        buttom = row - 1
        left = 0
        right = col - 1
        while left <= right and top <= buttom:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            for r in range(top, buttom + 1):
                res.append(matrix[r][right])
            right -= 1
            if not (left <= right and top <= buttom):
                break
            for c in range(right, left - 1, -1):
                res.append(matrix[buttom][c])
            buttom -= 1

            for r in range(buttom, top - 1,-1):
                res.append(matrix[r][left])
            left += 1

        return res
