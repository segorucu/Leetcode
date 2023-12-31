# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:


        ans = []
        def dfs(root,depth):
            if root:
                if depth > len(ans)-1:
                    ans.append([root.val])
                else:
                    ans[depth].append(root.val)
                dfs(root.left,depth+1)
                dfs(root.right,depth+1)


        dfs(root,0)
        ans.reverse()
        return ans





        