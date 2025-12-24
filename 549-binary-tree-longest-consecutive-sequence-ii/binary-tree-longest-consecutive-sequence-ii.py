# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        

        graph = defaultdict(list)
        nodeval = defaultdict(int)

        def dfs(root, ipar, icurr):
            if not root:
                return icurr

            if ipar >= 0:
                graph[ipar].append(icurr)
                graph[icurr].append(ipar)
            nodeval[icurr] = root.val
            ileft = dfs(root.left, icurr, icurr+1)
            iright = dfs(root.right, icurr, ileft+1)

            return iright

        dfs(root, -1, 0)

        visited = set()
        def dfs(node, increasing):
            visited.add(node)
            one = two = 0
            for neigh in graph[node]:
                if neigh in visited:
                    continue
                if increasing >= 0 and nodeval[neigh] == nodeval[node] + 1:
                    one = max(one, dfs(neigh, 1))
                if increasing <= 0 and nodeval[neigh] == nodeval[node] -1:
                    two = max(two, dfs(neigh,-1))
            return one + two + 1

        # print(graph, nodeval)
        final = 1
        for node in nodeval.keys():
            visited = set()
            if node not in visited:
                final = max(final, dfs(node, 0))

        return final