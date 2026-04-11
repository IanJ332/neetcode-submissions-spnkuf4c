class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 创建一个哨兵节点 (Dummy Node)，方便处理头节点变动的情况
        dummy = ListNode(0)
        dummy.next = head
        p_prev = dummy # p_prev 始终指向“要翻转的这一组”的前一个节点
        
        while True:
            # --- 第一步：探测够不够 k 个 ---
            curr = p_prev.next
            tail = p_prev
            for i in range(k):
                tail = tail.next
                if not tail: # 不够 k 个了，直接收工
                    return dummy.next
            
            # 记录下一组的开头 (比如 4)
            nxt_group_head = tail.next
            
            # --- 第二步：翻转当前组 [curr, nxt_group_head) ---
            # 这里的逻辑就是你刚才写的那个 while
            prev = nxt_group_head 
            temp = curr
            while temp != nxt_group_head:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            
            # --- 第三步：连接断掉的部分 ---
            # 此时这一组翻转完了，prev 是新的头 (3)，curr 变成了尾巴 (1)
            p_prev.next = prev
            p_prev = curr # 挪动 p_prev，准备处理下一组
            
        return dummy.next