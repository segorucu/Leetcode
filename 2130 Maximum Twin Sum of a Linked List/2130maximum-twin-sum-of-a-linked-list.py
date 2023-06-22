# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next

        nextnext = slow.next
        slow.next = None
        while nextnext:
            fast = nextnext
            nextnext = fast.next
            fast.next = slow
            slow = fast

        fast = slow
        slow = head

        ans = 0
        while fast:
            if fast.val + slow.val > ans:
                ans = fast.val + slow.val
            fast = fast.next
            slow = slow.next
        
        return ans