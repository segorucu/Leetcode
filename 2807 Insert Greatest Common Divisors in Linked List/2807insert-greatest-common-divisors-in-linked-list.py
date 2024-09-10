# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        while curr.next:
            next = curr.next
            node = ListNode(gcd(curr.val,next.val))
            curr.next, node.next = node, next
            curr = next


        return head
        