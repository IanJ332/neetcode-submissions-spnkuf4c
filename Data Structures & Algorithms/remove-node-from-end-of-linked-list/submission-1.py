# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 设置 dummy, slow, fast 和 counter
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        counter = 0
        # 2. 让 fast 先走 n 步
        while fast and counter != n:
            fast = fast.next
            counter += 1
        
        # 3. 同步移动直到 fast 走到尽头
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # 4. 删除节点并返回
        slow.next = slow.next.next
        return dummy.next