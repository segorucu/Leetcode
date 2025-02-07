# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        ans = []
        counter = collections.defaultdict(int)

        def decode(curr,node):
            if not node:
                curr.append("()")
                return 

            curr.append("(")
            curr.append(str(node.val))
            curr.append(")")
            decode(curr,node.left)
            decode(curr,node.right)


        def dfs(node):
            if node is None:
                return

            curr = []
            decode(curr,node)
            txt = "".join(curr)
            counter[txt] += 1
            if counter[txt] == 2:
                ans.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        return ans
        