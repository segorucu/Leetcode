class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:

        degree = collections.defaultdict(list)
        for a,b in edges:
            degree[a].append(b)
            degree[b].append(a)

        evens = set()
        odds = set()
        for i in range(1,n+1):
            if len(degree[i]) % 2 == 0:
                evens.add(i)
            else:
                odds.add(i)
        if len(odds) == 0:
            return True

        if not (len(odds) == 2 or len(odds) == 4):
            return False

        n = len(odds)
        print(degree,odds)
        odds = list(odds)
        if n == 2:
            one = odds[0]
            two = odds[1]
            # print(degree[one])
            # print(degree[two])
            if one not in degree[two]:
                return True
            for i in range(1,n+1):
                if i not in degree[one] and i not in degree[two]:
                    return True
            return False

        removed = set()
        def backtrack(i):
            if i == n:
                return False

            for j in range(n):
                if i != j and odds[i] not in removed and odds[j] not in removed:
                    if odds[i] not in degree[odds[j]]:
                        removed.add(odds[i])
                        removed.add(odds[j])
                        if len(removed) == n:
                            return True
                        res = backtrack(i+1)
                        if res:
                            return True
                        removed.remove(odds[i])
                        removed.remove(odds[j])
            return backtrack(i+1)
        res = backtrack(0)
        
        return res

        