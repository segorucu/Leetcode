# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:


        ans = []
        def dfs(root):
            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)
            if not left and not right:
                return root.val
            if not left:
                ans.append(right)
            elif not right:
                ans.append(left)
            return root.val


        dfs(root)
        return ans
        