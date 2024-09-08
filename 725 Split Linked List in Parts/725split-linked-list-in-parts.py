# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        size = len(arr) // k
        n = len(arr) % k
        ans = []
        p = 0
        for i in range(n):
            Sentinel = ListNode()
            curr = Sentinel
            for j in range(size+1):
                curr.next = ListNode(arr[p])
                curr = curr.next
                p += 1
            ans.append(Sentinel.next)

        n = k - n
        for i in range(n):
            Sentinel = ListNode()
            curr = Sentinel
            for j in range(size):
                curr.next = ListNode(arr[p])
                curr = curr.next
                p += 1
            ans.append(Sentinel.next)

        return ans

            

        