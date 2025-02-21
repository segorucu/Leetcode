# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def dfs(self, root):
        if root.left:
            root.left.val = root.val * 2 + 1
            self.visited.add(root.left.val)
            self.dfs(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self.visited.add(root.right.val)
            self.dfs(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        self.visited = set()
        self.tree.val = 0
        self.visited.add(0)
        self.dfs(self.tree)
        

    def find(self, target: int) -> bool:
        return target in self.visited
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)