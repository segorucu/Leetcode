# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next

        k = k % n

        dum = head
        if k == 0:
            return dum
        for _ in range(n-k):
            dum = dum.next

        
        for _ in range(n-k):
            tail.next = ListNode(head.val)
            tail = tail.next
            head = head.next
        

        return dum