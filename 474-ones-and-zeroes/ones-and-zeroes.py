class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        c1 = defaultdict()
        for i, st in enumerate(strs):
            c1[i] = Counter(st)

        @cache
        def dp(i,ones,zeros):
            if ones > n or zeros > m:
                return -1000
            if i == len(strs):
                return 0

            one = dp(i+1, ones + c1[i]['1'], zeros + c1[i]['0']) + 1
            two = dp(i+1, ones, zeros)
            return max(one, two)


        return dp(0, 0, 0)