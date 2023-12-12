# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 1:
            return head

        arr = []
        dummy = head
        arr.append(dummy)
        if dummy is None:
            return None
        for i in range(1,k):
            dummy = dummy.next
            arr.append(dummy)
            if dummy is None:
                return head
        firstnode = head
        lastnode = dummy

        firstnode.next = self.reverseKGroup(lastnode.next,k)

        for _ in range(1,k):
            node = arr.pop()
            node.next = arr[-1]

        return lastnode


