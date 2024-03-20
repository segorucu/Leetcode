# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        i = 0
        node = list1
        for i in range(b):
            if i == a-1:
                prea = node
            node = node.next
            
        b = node
        prea.next = list2
        node = list2
        while node.next:
            node = node.next
        node.next = b.next

        return list1

        