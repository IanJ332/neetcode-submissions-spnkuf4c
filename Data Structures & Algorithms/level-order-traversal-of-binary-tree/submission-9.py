# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 🛡️ 边界情况：如果 root 为空，返回 []。
        if not root:
            return []

        # 📦 初始化：创建最终的结果列表 res = []，以及队列 queue = deque([root])。
        res = []
        queue = deque([root])

        # 🔄 外层循环：while queue: 只要队列不为空就继续。
        while queue:
            # 🏷️ 每层准备：在 while 内部，先建一个空列表 level_value = [] 来存这一层的值。
            level_val = []

            # 📥 内层循环：用我们刚刚写好的 for _ in range(len(queue)): 弹出节点、存值、加入左右子节点。
            for _ in range(len(queue)):
                node = queue.popleft()
                level_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 💾 层级合并：在内层循环结束之后，把 level_value 放进大箱子 res 里面。
            res.append(level_val)
        return res