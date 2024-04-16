# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val,left = root)


        def dfs(root,currdepth):
            if not root:
                return

            if currdepth == depth-1:
                root.left = TreeNode(val,left=root.left)
                root.right =TreeNode(val,left=None,right=root.right)
            else:
                dfs(root.left,currdepth+1)
                dfs(root.right,currdepth+1)
            return

        dfs(root,1)
        return root