class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        
        counter = collections.defaultdict(collections.defaultdict)
        letters = set(s)
        for l in letters:
            counter[-1][l] = 0
        for i,a in enumerate(s):
            for l in letters:
                counter[i][l] = counter[i-1][l]
            counter[i][a] += 1 

        n = len(queries)
        ans = n * [0]
        for q in range(n):
            left, right = queries[q]
            curr = 0
            for l in letters:
                tmp = counter[right][l]- counter[left-1][l]
                curr += (tmp * (tmp+1)) // 2
            ans[q] = curr


        return ans