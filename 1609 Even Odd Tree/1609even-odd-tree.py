# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = collections.deque()
        queue.append(root)

        level = -1
        while queue:
            level += 1
            level = level % 2
            n = 0
            for _ in range(len(queue)):
                n += 1
                node = queue.popleft()
                if level == 0:
                    if node.val % 2 == 0:
                        return False
                    if n > 1 and node.val <= prev:
                        return False
                elif level == 1:
                    if node.val % 2 == 1:
                        return False
                    if n > 1 and node.val >= prev:
                        return False
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return True

