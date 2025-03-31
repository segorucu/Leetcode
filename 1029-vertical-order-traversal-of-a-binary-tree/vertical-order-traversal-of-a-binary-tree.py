# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        graph = defaultdict(lambda: defaultdict(list))

        queue = deque()
        queue.append((0,0,root))

        while queue:
            r, c, node = queue.popleft()
            graph[c][r].append(node.val)
            if node.left:
                queue.append((r+1,c-1,node.left))
            if node.right:
                queue.append((r+1,c+1,node.right))

        COLS = len(graph.keys())
        ans = []

        for col in sorted(graph.keys()):
            ans.append([])
            for row in sorted(graph[col].keys()):
                ans[-1].extend(sorted(graph[col][row]))

        return ans