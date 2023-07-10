# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        left = root.left
        right = root.right


        def symmetrictrees(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                return False

            res1 = symmetrictrees(p.left,q.right)
            res2 = symmetrictrees(p.right,q.left)

            return res1 and res2
            
        return symmetrictrees(left,right)