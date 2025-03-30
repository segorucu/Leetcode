"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None

        graph = {}
        def dfs(root):
            if not root:
                return 
            
            graph[root.val] = root
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        keys = list(sorted(graph.keys()))
        n = len(keys)
        for i,key in enumerate(keys):
            graph[key].left = graph[keys[(i-1)%n]]
            graph[key].right = graph[keys[(i+1)%n]]


        return graph[keys[0]]
        