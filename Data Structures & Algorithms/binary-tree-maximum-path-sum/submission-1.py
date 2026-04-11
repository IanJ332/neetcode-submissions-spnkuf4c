# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') # 初始化为极小值

        def gain(node):
            if not node:
                return 0
            
            # 1. 递归计算左右子树的单向最大收益
            # 如果收益是负的，我们直接要 0 (即“及时止损”)
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            
            # 2. 内政：检查以当前节点为“拱桥”的路径是否是全场最高
            current_bridge_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_bridge_sum)
            
            # 3. 外交：返回给父节点一个“单向最强收益”
            return node.val + max(left_gain, right_gain)

        gain(root)
        return self.max_sum
        