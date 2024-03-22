# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next is None:
            return True
        if head.next.next is None:
                return head.val == head.next.val

        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                break
            

        prev, curr = slow, slow.next
        i = 0
        while curr:
            if i == 0:
                prev.next, curr.next, prev, curr = None, prev, curr, curr.next
            else:
                curr.next, prev, curr = prev, curr, curr.next
            i += 1

        fast, slow = prev, head
        while fast:
            if slow.val != fast.val:
                return False
            slow, fast = slow.next, fast.next

        return True




