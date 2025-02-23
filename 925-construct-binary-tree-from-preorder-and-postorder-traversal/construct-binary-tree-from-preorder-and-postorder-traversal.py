# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(preorder,postorder):

            head = preorder[0]
            postorder.pop()
            tree = TreeNode(head)
            if len(preorder) > 1:
                leftval = preorder[1]
                ind = postorder.index(leftval)
                tree.left = dfs(preorder[1:ind+2], postorder[0:ind+1])
                if len(postorder) > ind + 1:
                    tree.right = dfs(preorder[ind+2:],postorder[ind+1:])
            return tree




        return dfs(preorder,postorder)


