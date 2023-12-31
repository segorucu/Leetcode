# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        queue = deque()
        if not root:
            return 0
        queue.append((root,1))

        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))

        return depth





        