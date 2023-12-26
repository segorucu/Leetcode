# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        def reverse(head,k):
            prev = None
            curr = head
            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return tail
                
        
        sentinel = ListNode(next=head)

        i = 1
        while i < left:
            head = head.next
            i += 1

        tail = head
        while i < right:
            tail = tail.next
            i += 1
        end = tail.next
        # print("tail",tail)


        node = reverse(head,right-left+1)
        # print("reversed",node)
        
        head.next = end
        # print("head",head)

        i = 1
        prehead = sentinel
        while i < left:
            prehead = prehead.next
            i += 1
        # print("prehead",prehead)

        prehead.next = node
        
        return sentinel.next
            

            
        