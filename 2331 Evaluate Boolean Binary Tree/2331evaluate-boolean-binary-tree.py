# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        mp = {0: False, 1: True, 2: lambda x, y: x or y, 3: lambda x, y: x and y}

        def dfs(node): 
            if not node.left:
                return  mp[node.val]

            return mp[node.val](dfs(node.left),dfs(node.right)) 



        return dfs(root)
        