# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ids = set()
        ids.add(head)

        while head:
            head = head.next
            if head in ids:
                return head
            ids.add(head)
        return head