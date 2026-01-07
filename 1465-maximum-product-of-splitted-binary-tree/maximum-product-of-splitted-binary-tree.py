# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        

        def calc_sum(root):
            if not root:
                return 0

            return root.val + calc_sum(root.left) + calc_sum(root.right)

        totalsm = calc_sum(root)
        
        def dfs(root):
            if not root:
                return 0, 0

            leftsm, leftans = dfs(root.left)
            rightsm, rightans = dfs(root.right)

            opt1 = leftsm * (totalsm - leftsm)
            opt2 = rightsm * (totalsm - rightsm)

            return leftsm + rightsm + root.val, max(leftans, rightans, opt1, opt2)

        MOD = 10**9+7
        return dfs(root)[1] % MOD
        