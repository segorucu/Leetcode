# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        mp = collections.defaultdict(list)

        curr = head
        while curr:
            mp[curr.val].append(curr)
            curr = curr.next

        Sentinel = ListNode()
        curr = Sentinel
        for key, val in sorted(mp.items()):
            for node in val:
                node.next = None
                curr.next = node
                curr = curr.next
                # print(key,Sentinel.next)

        return Sentinel.next
        