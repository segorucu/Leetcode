# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        depthmap = collections.defaultdict(list)

        def dfs(root):
            if not (root.left or root.right):
                depthmap[0].append(root.val)
                return None, 0

            dl = dr = 0
            if root.left:
                root.left, dl = dfs(root.left)
            if root.right:
                root.right, dr = dfs(root.right)
            currdepth = max(dl,dr) + 1
            depthmap[currdepth].append(root.val)
            return None, currdepth

        root, _ = dfs(root)
        ans = []
        for k,v in depthmap.items():
            ans.append(v)

        return ans

        