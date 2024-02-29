# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        def dfs(node):
            if not node:
                return 0


            l = dfs(node.left)
            r = dfs(node.right)
            if l + r == node.val:
                self.ans += 1
            return l + node.val + r


        dfs(root)
        return self.ans
        