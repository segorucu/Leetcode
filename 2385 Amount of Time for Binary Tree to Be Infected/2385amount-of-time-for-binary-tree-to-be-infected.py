# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        tab = defaultdict(list)
        def dfs(root):

            if root.left:
                tab[root.val].append(root.left.val)
                tab[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                tab[root.val].append(root.right.val)
                tab[root.right.val].append(root.val)
                dfs(root.right)


        dfs(root)
        
        queue = deque()
        queue.append((start,0))
        visited = set()
        while queue:
            node, level = queue.popleft()
            visited.add(node)
            for neigh in tab[node]:
                if neigh not in visited:
                    queue.append((neigh,level+1))

        return level
        