"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        def dfs(root):
            if not root:
                return None
            node = Node(root.val)
            if root.children:
                for child in root.children:
                    node.children.append(dfs(child))
            return node

        return dfs(root)