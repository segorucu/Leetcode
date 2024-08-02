# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans = []
        def dfs(node,curr):
            
            if not node:
                return 

            curr.append(str(node.val))
            if not node.left and not node.right:
                tmp = "->".join(curr)
                ans.append(tmp)

            dfs(node.left,curr)
            dfs(node.right,curr)
            curr.pop()


        dfs(root,[])
        return ans
        