# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        stack = []

        def dfs(node):
            if not node:
                return None, None
            
            dfs(node.left)
            stack.append(node)
            dfs(node.right)
            
        dfs(root)

        for i,node in enumerate(stack):
            if node.val == p.val:
                if i + 1 < len(stack):
                    return stack[i+1]
                else:
                    return None

        return None