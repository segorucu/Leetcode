# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        queue = deque()
        if not root:
            return []
        queue.append((root,0))
        ans = []
        while queue:
            node, depth = queue.popleft()
            if len(ans) <= depth:
                ans.append(node.val)
            else:
                ans[depth] = node.val
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
            
        return ans