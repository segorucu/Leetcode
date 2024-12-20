# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = collections.deque()
        mp = collections.defaultdict(list)
        queue.append((root,0))
        while queue:
            node, level = queue.popleft()
            mp[level].append(node)
            if node.left:
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))

        for key, nodelist in mp.items():
            if key % 2 == 1:
                l = 0
                r = len(nodelist)-1
                while l < r:
                    nodelist[l].val, nodelist[r].val = nodelist[r].val, nodelist[l].val
                    l += 1
                    r -= 1
        return root

        