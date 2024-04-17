# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.base = ord("a")
        self.ans = 8500*"z"
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(root,curr):
            if not root:
                return

            add = chr(self.base+root.val)
            if not root.left and not root.right:
                self.ans = min(self.ans,add+curr)
                return 

            dfs(root.left,add+curr)
            dfs(root.right,add+curr)

        dfs(root,"")
        return self.ans
        