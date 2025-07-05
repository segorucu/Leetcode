# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        while curr:
            prev = curr
            curr = curr.next
            while prev and curr and prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next

        return head
            