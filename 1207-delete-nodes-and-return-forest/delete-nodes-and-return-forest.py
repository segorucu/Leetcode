# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        ans = []
        def dfs(node):
            if not node:
                return None

            if node.val in to_delete:
                if node.left:
                    res = dfs(node.left)
                    if res:
                        ans.append(res)
                if node.right:
                    res = dfs(node.right)
                    if res:
                        ans.append(res)
                return None
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node

        res = dfs(root)
        if res:
            ans.append(res)
        return ans