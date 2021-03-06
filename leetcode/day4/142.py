from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = set()
         
        while head:
            if head in node_set:
                return head
            node_set.add(head)
            head = head.next
             
        return head