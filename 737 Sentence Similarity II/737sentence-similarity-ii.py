class UnionFind:
    def __init__(self,n):
        self.count = n
        self.parent = collections.defaultdict(str)
        self.rank = collections.defaultdict(int)

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        else:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        self.count -= 1




class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        n = len(sentence1)
        if n != len(sentence2):
            return False

        dictionary = set()
        for a,b in similarPairs:
            dictionary.update({a,b})
        m = len(dictionary)

        union = UnionFind(m)
        for word in dictionary:
            union.parent[word] = word
            union.rank[word] = 1

        for a,b in similarPairs:
            union.union(a,b)

        for word in dictionary:
            union.find(word)

        for a,b in zip(sentence1,sentence2):
            if a == b:
                continue
            elif a in union.parent and b in union.parent:
                if union.parent[a] == union.parent[b]:
                    continue
                else:
                    return False
            else:
                return False

    
        return True
        