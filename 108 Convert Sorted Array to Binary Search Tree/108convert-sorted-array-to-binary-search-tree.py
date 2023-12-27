# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left,right):
            if left > right:
                return None
            mid = (left+right) // 2
            if (left+right) % 2 == 1:
                mid += 1
            node = TreeNode(nums[mid])
            node.left = helper(left,mid-1)
            node.right = helper(mid+1,right)
            return node


        n = len(nums)
        return helper(0,n-1)