# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
          
        one = head
        two = head.next
        if two:
            sentinel = ListNode()
            sentinel.next = two
        else:
            return head

        # print(sentinel.next)
        while one:
            if not two:
                break
            else:
                three = two.next
                one.next = None
                two.next = one
                # print(sentinel.next)
                if three:
                    four = three.next
                    if four:
                        one.next = four
                        one = three
                        two = four
                    else:
                        one.next = three
                        break    
                elif not three:
                    break

        return sentinel.next

      
            

        return sentinel.next