# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        

        def dfs(root,direction):
            if not root:
                return 0

            if direction == "left" and not root.left and not root.right:
                return root.val
            left = dfs(root.left,"left")
            right = dfs(root.right,"right")
            return left + right





        return dfs(root,"")