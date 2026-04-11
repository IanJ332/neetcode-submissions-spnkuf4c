# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p and q are none
        if not p and not q:
            return True
        # if q or q one is none
        if not p or not q:
            return False
        # if p and q val not same
        if p.val != q.val:
            return False
        # recursive try following
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)