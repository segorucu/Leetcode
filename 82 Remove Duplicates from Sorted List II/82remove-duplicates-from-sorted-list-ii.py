# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        sentinel = ListNode()
        sentinel.next = head

        slow, fast = sentinel, sentinel.next.next
        corr = 0
        while fast:
            if slow.next.val == fast.val:
                fast = fast.next
                corr = 1
                continue
            if corr == 1:
                slow.next = fast
                fast = fast.next
            corr = 0
            if fast is None:
                break
            if slow.next.val != fast.val:
                slow = slow.next
                fast = fast.next
        if corr == 1:
            slow.next = fast

        return sentinel.next
