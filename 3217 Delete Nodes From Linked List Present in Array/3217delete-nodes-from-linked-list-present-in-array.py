# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)
        sentinel = ListNode(next=head)
        curr = sentinel.next
        prev = sentinel
        while curr:
            while curr and curr.val in nums:
                curr = curr.next
            prev.next = curr
            prev = curr
            if curr:
                curr = curr.next

        return sentinel.next