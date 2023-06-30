# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def solution(root):
            if root is None:
                return (float("inf"),None)

            if target < root.val:
                (mindiff, closest) = solution(root.left)
            else:
                (mindiff, closest) = solution(root.right)
                
            if abs(root.val - target) < mindiff:
                mindiff = abs(root.val - target)
                closest = root.val
            elif abs(root.val - target) == mindiff:
                closest = min(closest,root.val)
            return (mindiff,closest)
            
        return solution(root)[1]

        