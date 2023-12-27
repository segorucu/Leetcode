# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root):
            if not root:
                return 0

            found = 0
            if root.val in {p.val,q.val}:
                found += 1

            left = dfs(root.left)
            found += left
            right = dfs(root.right)
            found += right
            if found == 2 and not self.ans:
                self.ans = root

            return found

        dfs(root)
        return self.ans
        