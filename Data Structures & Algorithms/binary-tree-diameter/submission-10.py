# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 1. 悄悄记录并更新全局最大直径（左深度 + 右深度）
            self.max_diameter = max(self.max_diameter, left + right)
            
            # 2. 老老实实返回当前节点的高度给它的父节点
            return max(left, right) + 1
            
        dfs(root) # 开始递归
        return self.max_diameter # 返回记录下来的最大直径

        
                