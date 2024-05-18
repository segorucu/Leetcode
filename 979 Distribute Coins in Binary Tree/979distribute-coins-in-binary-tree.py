# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        def dfs(node):
            if not node:
                return 0

            L = dfs(node.left)
            R = dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + R + L - 1

        dfs(root)

        return self.ans

            
        