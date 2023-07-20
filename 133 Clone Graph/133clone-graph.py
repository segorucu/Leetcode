"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque, defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None
        if len(node.neighbors) == 0:
            return Node(1)

        queue = deque()
        queue.append(node)
        visited = defaultdict(list)
        nodedict = defaultdict(list)
        while queue:
            original = queue.popleft()
            if original.val in nodedict:
                copy = nodedict[original.val][0]
            else:
                copy = Node(original.val)
                nodedict[original.val].append(copy)
            for neigh in original.neighbors:
                if neigh.val not in nodedict:
                    queue.append(neigh)
                    neigh_copy = Node(neigh.val)
                    nodedict[neigh.val].append(neigh_copy)
                else:
                    neigh_copy = nodedict[neigh.val][0]
                if neigh.val not in visited[original.val]:
                    copy.neighbors.append(neigh_copy)
                    visited[copy.val].append(neigh.val)


        return nodedict[1][0]