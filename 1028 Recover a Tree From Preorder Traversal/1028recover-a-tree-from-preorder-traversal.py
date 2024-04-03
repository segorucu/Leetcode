# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        nodes = []
        r = 0
        n = len(traversal)
        while r < n:
            level = 0
            while traversal[r] == "-":
                r += 1
                level += 1
            beg = r
            while r < n and traversal[r] in "0123456789":
                r += 1
            val = int(traversal[beg:r])
            nodes.append((level,val))

        def dfs(arr):
            if not arr:
                return None
            node = TreeNode(arr[0][1])
            level = arr[0][0]
            next_level = level + 1
            p = 1
            while p < len(arr) and arr[p][0] != next_level:
                p += 1
            if p == n:
                return node
            leftp = p
            p += 1
            while p < len(arr) and arr[p][0] != next_level:
                p += 1
            rightp = p
            node.left = dfs(arr[leftp:rightp])
            if rightp == len(arr):
                node.right = None
            else:
                node.right = dfs(arr[rightp:])

            return node


        return dfs(nodes)

                