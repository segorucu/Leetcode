class UnionFind:
    def __init__(self,n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        self.count -= 1
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        union = UnionFind(n)

        visited = set()
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
        
            if l != -1:
                if l in visited:
                    return False
                visited.add(l)
                if not union.union(i,l):
                    return False
            if r != -1:
                if r in visited:
                    return False
                visited.add(r)
                if not union.union(i,r):
                    return False

        return union.count == 1
        