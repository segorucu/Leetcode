# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        rootval = [root.val]
        leftb = []
        rightb = []
        leaves = []

        ## status root: 0 leftb: 1 rightb: 2
        ## direction = "l", "r"

        def dfs(node, status):
            if not node:
                return

            if status != 0 and not (node.left or node.right):
                leaves.append(node.val)
            elif status == 1:
                leftb.append(node.val)
            elif status == 2:
                rightb.append(node.val)

            tmpl = tmpr = -1
            if status == 0:
                if node.left:
                    tmpl = 1
                if node.right:
                    tmpr = 2
            elif status == 1:
                if node.left:
                    tmpl = 1
                elif node.right:
                    tmpr = 1
            elif status == 2:
                if node.right:
                    tmpr = 2
                elif node.left:
                    tmpl = 2
                
            dfs(node.left, tmpl)
            dfs(node.right, tmpr)

        dfs(root, 0)

        return rootval + leftb + leaves + rightb[::-1]