# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node.left is None and node.right is None:
                return [node.val]
            left = []
            if node.left:
                left = dfs(node.left)
            right = []
            if node.right:
                right = dfs(node.right)
            return left + right

        return dfs(root1) == dfs(root2)
            