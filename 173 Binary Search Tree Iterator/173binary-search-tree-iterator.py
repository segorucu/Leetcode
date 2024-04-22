# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.arr = []
        self.pt = -1
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)

        dfs(root)
        self.n = len(self.arr)
        

    def next(self) -> int:
        self.pt += 1
        return self.arr[self.pt]
        

    def hasNext(self) -> bool:
        return self.pt+1 < self.n
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()