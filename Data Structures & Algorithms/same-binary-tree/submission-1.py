# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p and q are all None
        if not p and not q:
            return True
        # if p and q one of then is none, but the other one is not
        if not p or not q:
            return False
        # if p value and q value are not same
        if p.val != q.val:
            return False
        # if they all passed above, is good to have following, which is check if left and right are same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)