# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:

        counter = collections.defaultdict(int)
        while head:
            counter[head.val] += 1
            head = head.next

        Sentinel = ListNode()
        curr = Sentinel
        for k,v in counter.items():
            curr.next = ListNode(v)
            curr = curr.next
        return Sentinel.next
        