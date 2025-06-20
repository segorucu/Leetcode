# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if not node:
                return 0

            return dfs(node.left) + dfs(node.right) + node.val

        totsum = dfs(root)

        def dfs2(node):
            if not node:
                return 0, False
                
            leftsm, leftdec = dfs2(node.left)
            rightsm, rightdec = dfs2(node.right)

            tot = leftsm + rightsm + node.val
            if leftdec or rightdec:
                return tot, True

            if node.left and 2 * leftsm == totsum:
                return tot, True
            if node.right and 2 * rightsm == totsum:
                return tot, True

            return tot, False

        return dfs2(root)[1]
            



