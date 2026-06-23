class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        # ================= 第一步：二分查找锁定行 =================
        row_start = 0
        row_end = len(matrix) - 1
        ans_row = -1
        
        while row_start <= row_end:
            mid_row = (row_start + row_end) // 2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] < target:
                ans_row = mid_row      # 记录潜在的候选行
                row_start = mid_row + 1
            else:
                row_end = mid_row - 1
                
        # 如果连潜在的候选行都没有找到，说明 target 比矩阵里最小的数还小
        if ans_row == -1:
            return False
            
        # ================= 第二步：在一维行里复用二分查找 =================
        # 💡 提示：此时我们要查找的数组是目标行：target_list = matrix[ans_row]
        start = 0
        end = len(matrix[ans_row]) - 1
        
        while start <= end:
            mid = (start + end) // 2
            # 请在这里补全第二步的列查找逻辑：
            # 如果 matrix[ans_row][mid] == target -> 
            if matrix[ans_row][mid] == target:
                return True
            # 如果 matrix[ans_row][mid] < target -> ?
            if matrix[ans_row][mid] < target:
                start = mid + 1
            # 如果 matrix[ans_row][mid] > target -> ?
            if matrix[ans_row][mid] > target:
                end = mid - 1
            
        return False