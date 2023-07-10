from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(start,end):
            seen.add(start)
            if start not in table or end not in table: 
                return -1
            if start == end:
                return 1
            if end in table[start]:
                return table[start][end]
            else:
                for neighbor in table[start]:
                    if neighbor not in seen:
                        val = dfs(neighbor,end)
                        if val and val > 0:
                            val2 = table[start][neighbor]
                            return val * val2




        table = defaultdict(dict)
        for ratio,vals in zip(values,equations):
            x,y = vals[0],vals[1]
            table[x][y] = ratio
            table[y][x] = 1/ratio

        
        ans = []
        for x,y in queries:
            seen = set()
            val = dfs(x,y)
            if val:
                ans.append(val)
            else:
                ans.append(-1)

        return ans




