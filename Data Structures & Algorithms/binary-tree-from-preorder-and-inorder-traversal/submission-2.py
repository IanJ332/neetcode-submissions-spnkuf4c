# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 1. 确定根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. 找到根节点在 inorder 里的位置 (mid)
        mid = inorder.index(root_val)
        
        # 3. 递归构建左右子树
        # 左边：preorder 跳过根取 mid 个，inorder 取 mid 之前的所有
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0 : mid])
        
        # 右边：preorder 从 mid+1 开始取剩下所有，inorder 从 mid+1 开始取剩下所有
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root