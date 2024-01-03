# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -1000000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, max(left,0) + max(right,0) + root.val)
            return root.val + max(left,right,0)

        dfs(root)
        return self.ans



        dfs(root)
        