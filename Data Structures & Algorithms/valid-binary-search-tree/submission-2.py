# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # 队列里存：(当前节点, 该节点允许的最小值, 该节点允许的最大值)
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, low, high = queue.popleft()

            # 1. 核心检查：如果当前值越界了，直接判定非法
            if not (low < node.val < high):
                return False
            
            # 2. 存入左孩子：下限不变，上限变为当前值
            if node.left:
                queue.append((node.left, low, node.val))
            
            # 3. 存入右孩子：下限变为当前值，上限不变
            if node.right:
                queue.append((node.right, node.val, high))
            
        return True