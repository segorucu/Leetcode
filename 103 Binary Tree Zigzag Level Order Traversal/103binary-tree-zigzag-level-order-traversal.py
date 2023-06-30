# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            rowlength = len(queue)
            row = []
            for _ in range(rowlength):
                node = queue.popleft()
                row.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                           
            if len(ans) % 2 == 1:
                row.reverse()
                
            ans.append(row)
        return ans
                    
        
        