# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(root, tot):
            if not root:
                return True

            left = dfs(root.left, tot+root.val)
            if not left:
                root.left = None
            right = dfs(root.right, tot+root.val)
            if not right:
                root.right = None
            if not root.left and not root.right and tot + root.val < limit:
                return False

            if not left:
                if not right or root.right is None:
                    return False
            if not right:
                if not left or root.left is None:
                    return False
            return True

 
        res = dfs(root, 0)
        if not res:
            return None
        return root



        