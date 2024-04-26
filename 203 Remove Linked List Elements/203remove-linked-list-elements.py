# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        Sentinel = ListNode(next = head)

        prev = Sentinel
        curr = Sentinel.next
        # nxt = curr.next 
        while curr:
            while curr and curr.val == val:
                prev.next = curr.next
                curr = curr.next
            if curr:
                prev = curr
                curr = curr.next

        return Sentinel.next
        