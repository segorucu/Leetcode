# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None
        def dfs(root):
            if not root:
                return False, False

            pfound, qfound = False, False
            if root.val == p.val:
                pfound = True
            elif root.val == q.val:
                qfound = True

            pleft, qleft = dfs(root.left)
            pright, qright = dfs(root.right)
            nonlocal ans
            if ans is not None:
                return True, True
            pfinal = pfound or pleft or pright
            qfinal = qfound or qleft or qright
            if pfinal and qfinal:
                ans = root
            return pfinal, qfinal


        dfs(root)
        return ans
        