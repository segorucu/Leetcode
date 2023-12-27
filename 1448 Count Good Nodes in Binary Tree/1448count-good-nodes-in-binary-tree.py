# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,maxval):
            if not root:
                return 0

            sm = 0
            if root.val >= maxval:
                sm += 1
                maxval = root.val
            left = dfs(root.left,maxval)
            right = dfs(root.right,maxval)
            return left + right + sm


        return dfs(root,-float("inf"))

        