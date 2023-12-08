# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def preorder(node):
            if not node:
                return None
            elif node:
                left = preorder(node.left)
                right = preorder(node.right)
                ans = str(node.val) 
                if left:
                    ans += "("+str(left)+")"
                elif not left and right:
                    ans += "()"
                if right:
                    ans += "("+str(right)+")"
                return ans
                





        ans = preorder(root)
        return ans