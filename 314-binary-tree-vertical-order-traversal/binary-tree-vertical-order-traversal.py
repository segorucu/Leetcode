# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        rcdict = defaultdict(lambda: defaultdict(list))
        maxcols = [-1]
        def dfs (node, r, c):
            if not node:
                return
            maxcols[0] = max(maxcols[0],c)
            rcdict[r][c].append(node.val)

            dfs(node.left,r+1,c-1)
            dfs(node.right,r+1,c+1)


        dfs(root, 0, 0)
        if maxcols[0] == -1:
            return []

        cdict = defaultdict(list)
        for r in sorted(rcdict.keys()):
            for c in rcdict[r]:
                cdict[c].extend(rcdict[r][c])

        ans = []
        for c in sorted(cdict.keys()):
            ans.append(cdict[c])

        return ans



