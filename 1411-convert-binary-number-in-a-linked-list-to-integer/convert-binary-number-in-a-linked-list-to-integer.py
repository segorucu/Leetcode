# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        curr = head
        sm = 0
        while curr:
            sm = 2 * sm + curr.val
            curr = curr.next
        return sm