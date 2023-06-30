# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append(root)
        while queue:
            rowlength = len(queue)
            sm = 0
            for _ in range(rowlength):
                node = queue.popleft()
                sm += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                
        return sm
                
                
                
                
        
        
        