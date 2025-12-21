# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        finalans = [0]
        def dfs(root):
            if not root:
                return -10000000, 0 

            ans = 1
            leftval, leftlen = dfs(root.left)
            if leftval == root.val + 1:
                ans = max(ans, leftlen+1)
            rightval, rightlen = dfs(root.right)
            if rightval == root.val + 1:
                ans = max(ans, rightlen+1)
            finalans[0] = max(finalans[0], ans)
            return root.val, ans


        dfs(root)[1]
        return finalans[0]
        