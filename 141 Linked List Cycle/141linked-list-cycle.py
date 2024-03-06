# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ids = set()
        ids.add(head)

        while head:
            head = head.next
            if head in ids:
                return True
            ids.add(head)
        return False

        