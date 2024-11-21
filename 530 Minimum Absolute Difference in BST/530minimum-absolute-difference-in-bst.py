# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        def dfs(root):
            if not root:
                return 

            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)

    
        dfs(root)
        arr.sort()

        n = len(arr)
        mindiff = inf
        for i in range(1,n):
            mindiff = min(mindiff, arr[i]-arr[i-1])
        return mindiff
