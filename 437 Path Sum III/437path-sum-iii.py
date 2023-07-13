# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.count = 0
        graph = defaultdict(int)
        def dfs(node,graph,prefix):
            if not node:
                return
            prefix += node.val
            if prefix - targetSum in graph:
                self.count += graph[prefix-targetSum]
            
            graph[prefix] += 1

            dfs(node.left,graph,prefix)
            dfs(node.right,graph,prefix)

            graph[prefix] -= 1

        graph[0] = 1
        dfs(root,graph,0)

        return self.count

            