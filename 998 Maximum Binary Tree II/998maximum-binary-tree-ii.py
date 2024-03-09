# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def recurse(curr):
            if curr is None:
                return TreeNode(val)
            if curr.val < val:
                return TreeNode(val,left = curr, right =None)

            curr.right = recurse(curr.right)

            return curr
            


        return recurse(root)