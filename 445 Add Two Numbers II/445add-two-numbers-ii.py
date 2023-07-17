# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode()

        num = 0
        while l1:
            num = num * 10 + l1.val
            l1 = l1.next
        
        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        num = num + num2
        if num == 0:
            return ListNode()
        node = sentinel
        while num > 0:
            val = num % 10
            num = num // 10
            node.val =val
            sentinel = ListNode()
            sentinel.next = node
            node = sentinel
            

        return sentinel.next
