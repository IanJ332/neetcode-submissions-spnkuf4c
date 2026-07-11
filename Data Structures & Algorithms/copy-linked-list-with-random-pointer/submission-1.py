"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        old_to_new = {}
        
        # 1. 第一次遍历：创建所有新节点并建立映射
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # 2. 第二次遍历：连接新节点的 next 和 random 指针
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        # 3. 🏁 返回新链表的头节点
        # 应该返回什么呢？
        return old_to_new[head]