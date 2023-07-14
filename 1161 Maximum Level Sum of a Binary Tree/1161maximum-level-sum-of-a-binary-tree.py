# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque()
        queue.append(root)
        depth = 0
        maxsm = float("-inf")
        while queue:
            depth += 1
            sm = 0 
            for _ in range(len(queue)):
                node = queue.popleft()
                sm += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sm > maxsm:
                maxsm = sm
                maxind = depth
                
        return maxind
