# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        ans = [[0, None]]

        def dfs(root):
            if not root:
                return [inf, -inf, 0, True]

            minleft, maxleft, sizeleft, bstl = dfs(root.left)
            minright, maxright, sizeright, bstr  = dfs(root.right)
            size = sizeleft + sizeright + 1
            isbst = bstl and bstr
            if isbst and maxleft < root.val and minright > root.val:
                if size > ans[0][0]:
                    ans[0][0] = size
                    ans[0][1] = root
            else:
                isbst = False

            minval = min(minleft, minright, root.val)
            maxval = max(maxleft, maxright, root.val)
            return minval, maxval, size, isbst

        dfs(root)
        return ans[0][0]
