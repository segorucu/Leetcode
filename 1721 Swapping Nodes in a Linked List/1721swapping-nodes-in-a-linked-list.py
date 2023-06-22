# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(k-1):
            fast = fast.next
        swp = fast

        while fast.next:
            slow = slow.next
            fast = fast.next

        swp.val, slow.val = slow.val, swp.val

        return head