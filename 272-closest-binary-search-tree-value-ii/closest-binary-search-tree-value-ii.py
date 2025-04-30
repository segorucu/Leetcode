# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        ans = []
        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)

        ans.sort()
        hp = []
        for num in ans:
            heappush(hp,(-abs(num-target),num))
            if len(hp) > k:
                heappop(hp)

        ans = []
        while hp:
            _, val = heappop(hp)
            ans.append(val)

        return ans