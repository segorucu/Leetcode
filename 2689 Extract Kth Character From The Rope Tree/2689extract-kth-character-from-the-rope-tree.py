# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """

        text = []

        def dfs(node):
            if not node:
                return
            if node.len == 0:
                if len(node.val) > 0:
                    text.append(node.val)
            elif node.len > 0:
                left = dfs(node.left)
                right = dfs(node.right)

        dfs(root)
        text = ''.join(text)

        return text[k-1]