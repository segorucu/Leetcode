# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque()
        queue.append((root,0))
        stack = [[]]
        while queue:
            node, depth = queue.popleft()
            if len(stack) < depth+1:
                stack.append([])
            stack[-1].append(node.val)

            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))

        return stack

