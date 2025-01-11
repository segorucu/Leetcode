# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def add(l1,l2):
            head = ListNode()
            dummy = head
            carry = 0
            while l1 or l2 or carry > 0:
                sm = carry
                if l1:
                    sm += l1.val
                    l1 = l1.next
                if l2:
                    sm += l2.val
                    l2 = l2.next
                carry = sm // 10
                sm = sm % 10
                dummy.val = sm
                if l1 or l2 or carry > 0:
                    dummy.next = ListNode()
                    dummy = dummy.next
            return head

        sm = add(l1,l2)
        return sm