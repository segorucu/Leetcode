# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def check(counter):
            odd = 0
            for key, val in counter.items():
                if val % 2 == 1:
                    odd += 1
                if odd >= 2:
                    return 0
            
            return 1

        def dfs(node,counter):


            counter[node.val] += 1
            curr = l = r = 0
            if not node.left and not node.right:
                curr = check(counter)

            if node.left:
                l = dfs(node.left,counter)
            if node.right:
                r = dfs(node.right,counter)
            counter[node.val] -= 1
            
            
            return l + r + curr


        counter = collections.defaultdict(int)
        return dfs(root,counter)

        