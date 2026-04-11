# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p_prev = dummy
        while True:
            curr = p_prev.next
            tail = p_prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt_group_head = tail.next
            
            prev = nxt_group_head
            temp = curr
            while temp != nxt_group_head:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            
            p_prev.next = prev
            p_prev = curr
        return dummy.next
