# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:


        ans = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            sm = 0
            n = 0
            for _ in range(len(queue)):
                n += 1
                node = queue.popleft()
                sm += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sm/n)
        return ans
