# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        def bts(node):

            left = []
            right = []
            if node.left:
                left = bts(node.left)
            mid = [node.val]
            if node.right:
                right= bts(node.right)

            return left + mid + right

        arr = bts(root)

        def binarysearch(target):
            left = 0
            right = len(arr) - 1
            low = high = -5
            while left <= right:
                mid = (left+right) // 2
                if target == arr[mid]:
                    return [target,target]
                elif target > arr[mid]:
                    low = mid
                    left = mid + 1
                else:
                    high = mid
                    right = mid - 1

            if low == -5:
                return [-1,arr[0]]
            elif high == -5:
                return [arr[-1],-1]
            else:
                return [arr[low],arr[high]]

        ans = []
        for query in queries:
            ans.append(binarysearch(query))


        return ans