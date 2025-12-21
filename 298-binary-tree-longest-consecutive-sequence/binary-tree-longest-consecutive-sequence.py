# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        # finalans = [0]
        def dfs(root):
            if not root:
                return -10000000, 0, 0

            ans = 1
            fleft = fright = 1
            leftval, leftlen, fleft = dfs(root.left)
            if leftval == root.val + 1:
                ans = max(ans, leftlen+1)
            rightval, rightlen, fright = dfs(root.right)
            if rightval == root.val + 1:
                ans = max(ans, rightlen+1)

            return root.val, ans, max(fleft, fright, ans)


        return dfs(root)[2]
        # return finalans[0]
        