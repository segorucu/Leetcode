# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)

        def create_graph(child,parent):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            if child.left:
                create_graph(child.left,child)
            if child.right:
                create_graph(child.right,child)

        create_graph(root,None)

        visited = set()
        ans = []
        def dfs(node,distance):
            visited.add(node)
            if distance == 0:
                ans.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor,distance-1)

        dfs(target.val,k)

        return ans