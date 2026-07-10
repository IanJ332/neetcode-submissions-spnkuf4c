class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. 🐢🐇 快慢指针寻找链表中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. ✂️ 切断链表，并反转后半部分
        second = slow.next
        slow.next = None  # 断开前半部分
        
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
            
        # 3. 🤝 交替合并两半链表
        list1, list2 = head, prev  # prev 是反转后的新头节点
        while list2:
            nxt1 = list1.next
            nxt2 = list2.next
            
            list1.next = list2
            list2.next = nxt1
            
            list1 = nxt1
            list2 = nxt2