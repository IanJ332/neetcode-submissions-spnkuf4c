# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # left and right all none then true
        if p is None and q is None:
            return True
        # left have right none then is false
        if p is None or q is None:
            return False
        # left and right value not same is false
        if p.val != q.val:
            return False
        # return all
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)