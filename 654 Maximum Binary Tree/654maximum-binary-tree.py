# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def buildtree(arr):
            if len(arr) == 0:
                return None
            curr = max(arr)
            ind = arr.index(curr)

            return TreeNode(curr,buildtree(arr[0:ind]),buildtree(arr[ind+1:]))

        return buildtree(nums)