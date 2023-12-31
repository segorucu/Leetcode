# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        def helper(root):
            if not root:
                return None

            head = TreeNode(root.val)
            node = head
            if root.left:
                node.right = helper(root.left)
                node = node.right
            while node.right:
                node = node.right
            if root.right:
                node.right = helper(root.right)
            # print(head)
            return head
        
        
        head = helper(root)
        root.left = None
        node = root
        while head:
            head = head.right
            node.right = head
            node.left = None
            node = node.right
        
        return root
        