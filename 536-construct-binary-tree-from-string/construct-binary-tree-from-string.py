# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        arr = []
        i = 0
        while i < len(s):
            if s[i] not in {"(",")"}:
                j = i
                while j < len(s) and s[j] not in {"(",")"}:
                    j += 1
                arr.append(int(s[i:j]))
                i = j
            else:
                arr.append(s[i])
                i += 1
        

        def dfs(s):
            if not s:
                return
            Node = TreeNode(s[0])
            istart = 1

            if len(s) == istart:
                return Node

            paranthesis = 1
            istart += 1
            i = istart
            while paranthesis:
                if s[i] == "(":
                    paranthesis += 1
                elif s[i] == ")":
                    paranthesis -= 1
                i += 1

            Node.left = dfs(s[istart:i-1])
            if len(s) > i:
                Node.right = dfs(s[i+1:-1])
            return Node

        
        return dfs(arr)
        