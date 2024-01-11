# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def solution(root):
            if root is None:
                return None

            left = solution(root.left)
            right = solution(root.right)

            if left is None and right is None:
                return (root.val,root.val,0)

            if left is None:
                minval = min(right[0], root.val)
                maxval = max(right[1], root.val)
                diff = max(abs(minval-root.val),abs(maxval-root.val))
                maxdiff = max(diff,right[2])
                return (minval,maxval,maxdiff)

            if right is None:
                minval = min(left[0], root.val)
                maxval = max(left[1], root.val)
                diff = max(abs(minval-root.val),abs(maxval-root.val))
                maxdiff = max(diff,left[2])
                return (minval,maxval,maxdiff)

            minval = min(left[0], right[0], root.val)
            maxval = max(left[1], right[1], root.val)
            diff = max(abs(minval-root.val),abs(maxval-root.val))
            maxdiff = max(diff,left[2],right[2])
            return (minval,maxval,maxdiff)

        return solution(root)[2]
