# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:

        ind = 0
        count = 0
        while head and head.next:
            if head.val > head.next.val:
                count += 1
            else:
                count -= 1
            head = head.next.next

        if count == 0:
            return "Tie"
        elif count > 0 :
            return "Even"
        else:
            return "Odd"
        