# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        # ans = []
        def dfs(root):
            if not root:
                return root

            if root.left:
                left = dfs(root.left)
            else:
                return TreeNode(root.val)
            # if root.right:
            #     right =dfs(root.right)
            node = left
            while left.right:
                left = left.right
            left.right = TreeNode(root.val)
            if root.right:
                left.left = TreeNode(root.right.val)
            return node




        return dfs(root)
        