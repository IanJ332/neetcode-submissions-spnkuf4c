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
        oldcopy = {None: None}

        curr = head
        while curr: 
            copy = Node(curr.val)
            oldcopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldcopy[curr]
            copy.next = oldcopy[curr.next]
            copy.random = oldcopy[curr.random]
            curr = curr.next

        return oldcopy[head]