# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(node):
            if not node:
                return []
            left = inorder(node.left)
            right = inorder(node.right)
            return left + [node.val] + right

        arr1 = inorder(root1)
        arr2 = inorder(root2)
        r1 = r2 = 0
        ans = []
        while r1 < len(arr1) and r2 < len(arr2):
            if arr1[r1] < arr2[r2]:
                ans.append(arr1[r1])
                r1 += 1
            elif arr1[r1] > arr2[r2]:
                ans.append(arr2[r2])
                r2 += 1
            else:
                ans.extend([arr1[r1],arr2[r2]])
                r1 += 1
                r2 += 1

        while r1 < len(arr1):
            ans.append(arr1[r1])
            r1 += 1
        while r2 < len(arr2):
            ans.append(arr2[r2])
            r2 += 1
        return ans