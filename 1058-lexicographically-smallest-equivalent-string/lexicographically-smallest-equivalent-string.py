class UnionFind:
    def __init__(self,n,letters):
        self.parent = {}
        for letter in letters:
            self.parent[letter] = letter
        self.n = n

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        letters = set(s1) | set(s2) | set(baseStr)
        union = UnionFind(len(letters),letters)

        for a,b in zip(s1,s2):
            if a != b:
                union.union(a,b)

        for letter in letters:
            union.find(letter)

        # print(union.parent)
        ans = []
        for letter in baseStr:
            # print(letter, union.parent[letter])
            ans.append(union.parent[letter])

        return "".join(ans)

        
