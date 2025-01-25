class UnionFind:
    def __init__(self,n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        
        if self.rank[px] <= self.rank[py]:
            self.rank[py] += self.rank[px]
            self.parent[px] = py
        else:
            self.rank[px] += self.rank[py]
            self.parent[py] = px
            
        self.count -= 1

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        stack = []
        for i,num in enumerate(nums):
            stack.append((num,i))
        stack.sort()

        n = len(nums)
        union = UnionFind(n)
        for i in range(1,n):
            if i > 0:
                if stack[i][0] <= stack[i-1][0] + limit:
                    union.union(stack[i][1],stack[i-1][1])

        mp = collections.defaultdict(list)
        imp = collections.defaultdict(list)
        for i in range(n):
            j = union.parent[i]
            mp[j].append(nums[i])
            imp[j].append(i)

        for key in mp:
            mp[key].sort()
            imp[key].sort()

        ans = n * [0]
        for key in mp:
            m = len(mp[key])
            for i, val in zip(imp[key],mp[key]):
                ans[i] = val


        return ans
        