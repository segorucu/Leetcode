# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = collections.defaultdict(int)
        stack = []
        nmstack = []
        seen  = set()

        curr = head
        sm = 0
        while curr:
            sm += curr.val
            if curr.val == 0:
                pass
            else:
                if sm == 0:
                    stack = []
                    nmstack = []
                elif sm in stack:
                    while stack[-1] != sm:
                        stack.pop()
                        nmstack.pop()
                else:
                    stack.append(sm)
                    nmstack.append(curr.val)
            curr = curr.next

        Sentinel = ListNode()
        curr = Sentinel
        for val in nmstack:
            curr.next = ListNode(val)
            curr = curr.next
            

        return Sentinel.next
                    

            
            


        return Sentinel.next