# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = collections.defaultdict(list)

        if not head or not head.next:
            return head

        curr = head
        while curr:
            nodes[curr.val].append(curr)
            curr = curr.next

        nodelist = list(nodes.keys())
        nodelist.sort()
        one = two = None
        for nodeval in nodelist:
            for node in nodes[nodeval]:
                two = node
                if one:
                    one.next = two
                one = two

        two.next = None

        return nodes[nodelist[0]][0]

        