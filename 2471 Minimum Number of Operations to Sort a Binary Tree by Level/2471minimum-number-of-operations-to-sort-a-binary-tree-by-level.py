# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        levelmp = collections.defaultdict(list)
        def dfs(root,level):
            if not root:
                return
            levelmp[level].append(root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)

        dfs(root,0)
        ops = 0
        for key, arr in levelmp.items():
            goal = arr.copy()
            goal.sort()
            curr = collections.defaultdict(int)
            for i,val in enumerate(arr):
                curr[val] = i
            for i, val in enumerate(goal):
                one = goal[i]
                two = arr[i]
                if one != two:
                    j = curr[goal[i]]
                    curr[one] = i
                    curr[two] = j
                    arr[i], arr[j] = arr[j], arr[i]
                    ops += 1

            

        return ops