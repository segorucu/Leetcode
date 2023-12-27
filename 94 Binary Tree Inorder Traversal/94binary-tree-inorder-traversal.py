# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        def dfs(root):
            if root:
                left = dfs(root.left)
                if left:
                    ans.extend(left)
                ans.append(root.val)
                right = dfs(root.right)
                if right:
                    ans.extend(right)


        dfs(root)
        return ans

        