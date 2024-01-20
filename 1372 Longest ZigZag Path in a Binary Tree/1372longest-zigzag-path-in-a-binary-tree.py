# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node,direc,cost):
            if not node:
                return cost

            if direc == "l":
                left = dfs(node.left,"l",0)
                right = dfs(node.right,"r",cost+1)
            else:
                left = dfs(node.left,"l",cost+1)
                right = dfs(node.right,"r",0)

            return max(left,right)

        left = dfs(root.left,"l",0)
        right = dfs(root.right,"r",0)

        return max(left,right)