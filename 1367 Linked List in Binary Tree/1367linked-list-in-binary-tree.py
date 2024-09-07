# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        curr = head
        search = []
        while curr:
            search.append(curr.val)
            curr = curr.next

        arr = []
        m = len(search)
        def dfs(node):
            if not node:
                return False

            arr.append(node.val)
            if arr[-m:] == search[:]:
                return True

            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            arr.pop()
            return False


        return dfs(root)
        