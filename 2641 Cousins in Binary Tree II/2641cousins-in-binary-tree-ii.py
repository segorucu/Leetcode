# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        levelsm = collections.defaultdict(int)
        parent_dict = collections.defaultdict(int)
        def dfs(parent,node,level):
            if not node:
                return
            parent_dict[parent] += node.val 
            levelsm[level] += node.val
            dfs(node, node.left, level+1)
            dfs(node, node.right, level+1)

        dfs(-1,root, 0)

        # print(levelsm, parent_dict.values())

        def dfs(parent, node, level):
            if not node:
                return

            node.val = levelsm[level] - parent_dict[parent]
            dfs(node, node.left, level+1)
            dfs(node, node.right, level+1)



        dfs(-1, root, 0)
        return root