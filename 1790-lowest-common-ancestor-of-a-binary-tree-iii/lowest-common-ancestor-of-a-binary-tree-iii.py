"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def dfs(node,ref):
            if not node:
                return False
            if node.val == ref.val:
                return True

            return dfs(node.left,ref) or dfs(node.right,ref)

        if dfs(p,q):
            return p
        if dfs(q,p):
            return q

        visited = set()
        queue = deque()
        queue.append(p)
        queue.append(q)
        while queue:
            node = queue.popleft()
            if node in visited:
                return node
            visited.add(node)
            if node.parent:
                queue.append(node.parent)

