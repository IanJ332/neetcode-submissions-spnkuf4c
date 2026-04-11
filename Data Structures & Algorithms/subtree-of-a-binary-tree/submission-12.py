class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. 基础情况：大树找空了都没找到
        if not root: 
            return False
        
        # 2. 核心判断：
        #    要么当前这棵树就是 (isSameTree)
        #    要么在左子树里找 (isSubtree)
        #    要么在右子树里找 (isSubtree)
        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)