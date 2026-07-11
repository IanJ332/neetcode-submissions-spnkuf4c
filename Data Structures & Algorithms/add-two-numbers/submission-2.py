# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        
        while l1 or l2 or carry != 0:
            # 🛡️ 安全获取当前位的值
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # ➕ 计算总和与进位
            total = v1 + v2 + carry
            num = total % 10
            carry = total // 10
            
            # 🔗 串联新节点
            tail.next = ListNode(num)
            tail = tail.next
            
            # 🏃‍♂️ 安全移动原链表指针
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # 🏁 返回结果
        # 思考线：我们应该返回什么？
        return dummy.next
