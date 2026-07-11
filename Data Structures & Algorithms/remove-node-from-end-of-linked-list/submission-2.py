# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        counter = 0
        slow, fast = dummy, dummy

        while fast and counter != n:
            fast = fast.next
            counter += 1

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next
