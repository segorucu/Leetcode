# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxdiff = 0

        def solution(root):
            if root is None:
                return 0

            left = solution(root.left)
            right = solution(root.right)


            self.maxdiff = max(self.maxdiff,left+right)
            return max(left,right)+1

        solution(root)
        return self.maxdiff






        
