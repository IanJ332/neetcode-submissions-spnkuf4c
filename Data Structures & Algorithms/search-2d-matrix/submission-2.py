class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)     # 总行数
        n = len(matrix[0])  # 总列数
        
        # 1. 把二维矩阵看作一维数组，初始化 start 和 end 索引
        start = 0
        end = m * n - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            # 2. 🌟 运用核心公式，将一维索引 mid 转换为矩阵的 row 和 col
            row = mid // n
            col = mid % n
            
            # 3. ⚖️ 接下来和标准二分查找完全一样
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                # 💡 请补全最后一种情况：当矩阵中的值大于 target 时，end 该怎么更新？

                if matrix[row][col] > target:
                    end = mid - 1
                
        return False