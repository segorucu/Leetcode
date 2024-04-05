# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        mp = collections.defaultdict(list)
        def dfs(root):
            if root.left:
                mp[root.val].append((root.left.val,"L"))
                mp[root.left.val].append((root.val,"U"))
                dfs(root.left)
            if root.right:
                mp[root.val].append((root.right.val,"R"))
                mp[root.right.val].append((root.val,"U"))
                dfs(root.right)
            
        dfs(root)

        path = []
        visited = set()
        def dfs2(node):
            visited.add(node)
            if node == destValue:
                return True
            for neigh,dr in mp[node]:
                if neigh in visited:
                    continue
                path.append(dr)
                if dfs2(neigh):
                    return True
                path.pop()


        dfs2(startValue)
        return "".join(path)

