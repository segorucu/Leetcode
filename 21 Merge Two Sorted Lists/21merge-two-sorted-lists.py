# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            node1 = head.next
            node2 = list2
        else:
            head = list2
            node1 = list1
            node2 = head.next


        curr = head
        # print(node1,node2,head)
        while node1 and node2:
            # print("iter",node1.val,node2.val)
            if node1.val <= node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next
            # print(node1)
            # print(node2)
            # print(head)
        # print(node1)
        # print(node2)
        # print(curr)
        # print(head)
        if node1:
            curr.next = node1
        elif node2:
            curr.next = node2

        return head


        return head