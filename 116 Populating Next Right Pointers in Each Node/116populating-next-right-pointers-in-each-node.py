"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque()
        queue.append((root,0))

        lasti = -1
        while queue:
            node, i = queue.popleft()
            if i == lasti:
                prev.next = node
            elif i > lasti:
                lasti = i
            prev = node
            if node.left:
                queue.append((node.left,i+1))
            if node.right:
                queue.append((node.right,i+1))

        return root

        