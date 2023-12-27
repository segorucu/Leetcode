# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        def bst(root):
            if not root:
                return 0.0, 0, 0.0

            sm = root.val
            lmean, ln, lmaxval = bst(root.left)
            rmean, rn, rmaxval = bst(root.right)
            ntot = rn+ln+1
            mean = (root.val + lmean*ln + rmean*rn) / (ntot)
            maxval = max(lmaxval,rmaxval,mean)
            return mean, ntot, maxval


        return bst(root)[2]
        