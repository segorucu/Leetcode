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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1


        def helper(root,right):
            if right < 0:
                return None
            
            mid = right // 2
            if right % 2 == 1:
                mid += 1

            midnode = root
            for _ in range(mid):
                midnode = midnode.next
            tree = TreeNode(midnode.val)
            tree.left = helper(root,mid-1)
            tree.right = helper(midnode.next,right-mid-1)
            return tree

        tree =helper(head,n-1)

        return tree

        