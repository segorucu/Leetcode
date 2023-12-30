# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.p = 0
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def swap(root,minbound,maxbound):
            if not root:
                return float("inf"), float("inf")

            if root.val <= minbound:
                dum = root.val
                root.val = minbound
                return minbound, dum
            elif root.val >= maxbound:
                dum = root.val
                root.val = maxbound
                return maxbound, dum

            l1, l2 = swap(root.left,minbound,root.val)
            if root.val == l1:
                root.val = l2
            if l1 != float("inf"):
                return l1, l2
            r1, r2 = swap(root.right,root.val,maxbound)
            if root.val == r1:
                root.val = r2
            if r1 != float("inf"):
                return r1,r2
            return float("inf"), float("inf")


        swap(root,-float("inf"),float("inf"))

        return root