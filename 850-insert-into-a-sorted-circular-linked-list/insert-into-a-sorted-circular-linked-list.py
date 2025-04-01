"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        if not head:
            curr = Node(insertVal)
            curr.next = curr
            return curr

        if head.next == head:
            head.next = Node(insertVal)
            curr = head.next
            curr.next = head
            return head

        curr = head
        visited = set()
        prev = None
        maxnode = None
        while curr not in visited:
            # print(prev, curr.val, curr.next.val)
            if prev and prev <= curr.val and curr.val > curr.next.val:
                    maxnode = curr
            prev = curr.val

            visited.add(curr)
            if curr.val <= insertVal <= curr.next.val:
                nxt = curr.next
                curr.next = Node(insertVal)
                curr = curr.next
                curr.next = nxt
                return head
            curr = curr.next

        if not maxnode:
            maxnode = head
        nxt = maxnode.next
        maxnode.next = Node(insertVal)
        curr = maxnode.next
        curr.next = nxt

        return head