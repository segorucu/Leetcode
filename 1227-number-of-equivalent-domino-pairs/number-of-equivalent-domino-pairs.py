class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        

        counter = defaultdict(int)
        ans = 0
        for col in dominoes:
            col.sort()
            col = tuple(col)
            ans += counter[col]
            counter[col] += 1

        return ans