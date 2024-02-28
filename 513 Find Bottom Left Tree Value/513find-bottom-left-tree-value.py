# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        layer = {}

        def dfs(node,row):
            if not node:
                return row

            if row not in layer:
                layer[row] = node.val
            l = dfs(node.left,row+1)
            r = dfs(node.right,row+1)
            return max(l,r)


        row = dfs(root,0)
        return layer[row-1]
        