"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None

        def flatten(root):
            if not root:
                return None, None

            tail1, head1 = flatten(root.left)
            if head1:
                head1.right = root
                root.left = head1
            tail2, head2 = flatten(root.right)
            if tail2:
                root.right = tail2
                tail2.left = root

            if tail1:
                tail = tail1
            else:
                tail = root

            if head2:
                head = head2
            else:
                head = root

            return tail, head


        tail, head = flatten(root)
        tail.left = head
        head.right = tail
    
        return tail
        