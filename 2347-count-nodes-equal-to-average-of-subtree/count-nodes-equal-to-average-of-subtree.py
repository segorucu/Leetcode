# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        counter = [0]
        def dfs(root):
            if not root:
                return 0, 0

            currval = root.val
            leftsm, leftn = dfs(root.left)
            rightsm, rightn = dfs(root.right)
            totsm = leftsm + rightsm + currval
            totn = leftn + rightn + 1
            if totsm // totn == currval:
                counter[0] += 1

            return totsm, totn

        dfs(root)
        return counter[0]