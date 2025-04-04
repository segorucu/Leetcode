# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root,depth):
            if not root:
                return None, None

            depth_l, ancestor_l = dfs(root.left,depth+1)
            depth_r, ancestor_r = dfs(root.right,depth+1)

            if not (depth_l or depth_r):
                return depth, root
            elif not depth_l:
                return depth_r, ancestor_r
            elif not depth_r:
                return depth_l, ancestor_l
            elif depth_l < depth_r:
                return depth_r, ancestor_r
            elif depth_r < depth_l:
                return depth_l, ancestor_l
            elif depth_l == depth_r:
                return depth_l, root
            
    
        return dfs(root,0)[1]