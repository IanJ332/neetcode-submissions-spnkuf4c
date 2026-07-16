# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return (self._isSametree(root, subRoot) or
        self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
    
    def _isSametree(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self._isSametree(node1.left, node2.left) and self._isSametree(node1.right, node2.right)