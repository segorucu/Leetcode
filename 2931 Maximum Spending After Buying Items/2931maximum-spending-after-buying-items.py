class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:

        m = len(values)
        n = len(values[0])
        mp = {}
        for i in range(m):
            mp[i] = []
            for j in range(n):
                mp[i].append(values[i][j]) 

        day = 0
        ans = 0
        while day < m*n:
            day += 1
            smallest = inf
            for key, values in mp.items():
                val = values[-1]
                if val < smallest:
                    smallest = val
                    selected = key
            val = mp[selected].pop()
            ans += val * day
            if len(mp[selected]) == 0:
                del mp[selected]
            

        return ans


        