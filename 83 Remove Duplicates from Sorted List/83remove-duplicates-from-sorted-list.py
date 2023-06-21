# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        if head is None:
            return head
        fast = head.next

        
        while fast:
            while slow.val == fast.val:
                slow.next = fast.next
                fast.val = None
                fast = fast.next
                if fast is None:
                    return head
            if fast:
                slow = slow.next
                fast = fast.next
            
        return head
        