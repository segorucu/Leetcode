# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # if node is a leaf, return leaf, depth
        # if node has one child, return child's output
        # if node has two children, but one child goes deeper, return that child's output
        # if node has two children and both have same depth, return node, child's depth


        def dfs(node, depth):
            if not (node.left or node.right):
                return node, depth

            if not node.left:
                return dfs(node.right, depth+1)
            if not node.right:
                return dfs(node.left, depth+1)

            leftchild, leftdepth = dfs(node.left, depth+1)
            rightchild, rightdepth = dfs(node.right, depth+1)

            if leftdepth == rightdepth:
                return node, leftdepth

            if leftdepth > rightdepth:
                return leftchild, leftdepth
            else:
                return rightchild, rightdepth



        return dfs(root, 0)[0]