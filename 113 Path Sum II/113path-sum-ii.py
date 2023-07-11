# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        stack = []

        def recurseTree(node,pathNodes,totalSum):
            if not node:
                return
            pathNodes.append(node.val)
            totalSum += node.val
            if totalSum == targetSum and not node.left and not node.right:
                stack.append(list(pathNodes))
            else:
                recurseTree(node.left,pathNodes,totalSum)
                recurseTree(node.right,pathNodes,totalSum)
            pathNodes.pop()

        recurseTree(root,[],0)

        return stack
