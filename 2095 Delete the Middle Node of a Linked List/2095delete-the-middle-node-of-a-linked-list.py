# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next is None:
            return None
        if head.next.next is None:
            head.next = None
            return head

        slow = head
        fast = head.next.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                break

        slow.next = slow.next.next
        return head

        

        
