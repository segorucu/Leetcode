# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val < q.val:
            sm = p.val
            bg = q.val
        else:
            sm = q.val
            bg = p.val

        while True:
            if root.val > bg:
                root = root.left
            elif root.val < sm:
                root = root.right
            else:
                return root
        return root
        