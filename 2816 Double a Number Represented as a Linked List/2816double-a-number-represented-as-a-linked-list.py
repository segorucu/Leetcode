# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        num = 0
        while curr:
            num = 10 * num + curr.val
            curr = curr.next
        num  *= 2
        arr = []
        while num > 0:
            num, rem = divmod(num, 10)
            arr.append(rem)
        arr = list(reversed(arr))
        if not arr:
            arr.append(0)

        i = 0
        curr = head
        while curr:
            curr.val = arr[i]
            if curr.next:
                curr = curr.next
                i += 1
            else:
                break
        if len(arr) == i+2:
            curr.next = ListNode(arr[-1])

        return head
        