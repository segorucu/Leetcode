# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def __init__(self):
        self.ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(root):
            if not root:
                return 0
            # print(root.val)
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            if (abs(left-right)) > 1:
                self.ans = False
            return(max(left,right))

        dfs(root)

        return self.ans


        