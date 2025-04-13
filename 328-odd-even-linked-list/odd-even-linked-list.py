# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next or not head.next.next:
            return head

        OddSentinel = ListNode()
        Odd = OddSentinel
        EvenSentinel = ListNode()
        Even = EvenSentinel
        
        curr = head
        while curr and curr.next:
            Odd.next = curr
            Even.next = curr.next
            curr = curr.next.next
            Odd = Odd.next
            Even = Even.next
        Even.next = None
        if curr:
            Odd.next = curr
            Odd = Odd.next
        Odd.next = EvenSentinel.next
        # print(curr)

        return OddSentinel.next

        
        