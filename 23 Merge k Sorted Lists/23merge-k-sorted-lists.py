# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        k = len(lists)
        sentinel = ListNode()
        tail = sentinel

        arr = []
        for i in range(k):
            curr = lists[i]
            while curr:
                arr.append(curr.val)
                curr = curr.next

        heapq.heapify(arr)
        while arr:
            val = heapq.heappop(arr)
            tail.next = ListNode(val)
            tail = tail.next
        

        return sentinel.next
        