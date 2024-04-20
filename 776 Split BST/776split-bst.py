# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        stack = []

        def dfs(root):
            if not root:
                return [None, None]

            if root.val <= target:
                left, right = dfs(root.right)
                root.right = left
                return [root, right]
            else:
                left, right = dfs(root.left)
                root.left = right
                return [left, root]
                


        
        return dfs(root)
