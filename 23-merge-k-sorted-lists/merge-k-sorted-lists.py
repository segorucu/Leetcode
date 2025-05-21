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

        arr.sort(reverse = True)
        while arr:
            val = arr.pop()
            tail.next = ListNode(val)
            tail = tail.next
        

        return sentinel.next
        