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
        high = float('inf')
        low = float('-inf')
        queue = deque([(root, high, low)])

        while queue:
            node, high, low = queue.popleft()

            if node.val <= low or node.val >= high:
                return False
            
            if node.left: queue.append((node.left, node.val, low))
            if node.right: queue.append((node.right, high, node.val))

        return True
