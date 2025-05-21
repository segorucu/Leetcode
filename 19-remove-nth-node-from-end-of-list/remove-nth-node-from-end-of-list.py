# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next

        if sz - n == 0:
            return head.next

        k = sz - n - 1
        curr = head
        while k:
            curr = curr.next
            k -= 1

        if curr.next and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        

        
        return head
 
        