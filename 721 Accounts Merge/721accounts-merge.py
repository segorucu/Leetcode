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
            return
        if px <= py:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        self.count -= 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)
        union = UnionFind(n)
        mailtoind = {}
        for i, account in enumerate(accounts):
            person = account[0]
            for j in range(1,len(account)):
                mail = account[j]
                if mail in mailtoind:
                    y = mailtoind[mail]
                    union.union(i,y)
                else:
                    mailtoind[mail] = i
        
        ans = [[] for i in range(union.count)]
        visited = set()
        accounttojoint = {}
        lastrow = -1
        visitedmail = set()
        namelist = {}
        for row in range(n):
            account = accounts[row]
            name = account[0]
            parent = union.find(row)
            if parent not in visited:
                lastrow += 1
                accounttojoint[parent] = lastrow
                namelist[lastrow] = [name]
                visited.add(parent)
                currrow = lastrow
            elif parent in visited:
                currrow = accounttojoint[union.parent[row]]
            for i in range(1,len(account)):
                mail = account[i]
                if mail not in visitedmail:
                    ans[currrow].append(mail)
                visitedmail.add(mail)

        for i,row in enumerate(ans):
            row.sort()
            ans[i] = namelist[i] + row[:]


        return ans
