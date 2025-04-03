# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0

            ansl, left = dfs(node.left)
            ansr, right = dfs(node.right)

            ret = max(left,right)+1
            ans = max(ansl, ansr, left+right+1)
            # print(node.val, ans, ret)
            return ans, ret

        return dfs(root)[0]-1

        