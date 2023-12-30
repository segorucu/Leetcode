# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.ans = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(root,minbound,maxbound):
            if not root:
                return True

            if minbound < root.val < maxbound:
                pass
            else:
                return False

            left = inorder(root.left,minbound,root.val)
            right = inorder(root.right,root.val,maxbound)
            return left and right

        
        return inorder(root,-float("inf"),float("inf"))

                
