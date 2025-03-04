# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        n = len(inorder)
        def build(preorder,inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = build(preorder[1:mid+1],inorder[0:mid])
            root.right = build(preorder[mid+1:],inorder[mid+1:])
            return root
            
        
        return build(preorder,inorder)
        