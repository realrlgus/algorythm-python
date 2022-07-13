from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        cur = head
        while cur:
            counter += 1
            cur = cur.next
        middle = int(counter / 2)

        for _ in range(middle):
            head = head.next
        return head