# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        nodes = defaultdict(int)
        i = 0
        curr = head
        while curr:
            nodes[i] = curr
            curr = curr.next
            i += 1

        left, right = 0, i-1
        prev = None
        while left < right:
            if prev:
                prev.next = nodes[left]
            nodes[left].next = nodes[right]
            prev = nodes[right]
            left += 1
            right -= 1
        if i % 2 == 0:
            nodes[right+1].next = None
        else:
            prev.next = nodes[left]
            nodes[left].next = None


        return head