# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = []
        def dfs(root,path):
            if not root:
                return
            if not (root.left or root.right):
                path.append(root.val)
                ans.append(path[:])
                path.pop()
                return

            path.append(root.val)
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()

        dfs(root,[])
        tot = 0
        for arr in ans:
            it = 0
            sm = 0
            while arr:
                a = arr.pop()
                sm += a * 10 ** it
                it += 1
            tot += sm
        return tot