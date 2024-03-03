# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = fast = head
        count = 0
        while fast:
            fast = fast.next
            if count > n:
                slow = slow.next
            count +=1
        if slow.next is None:
            return None
        if count == n and slow == head:
            head = head.next
            return head

        slow.next = slow.next.next

        return head
 
        