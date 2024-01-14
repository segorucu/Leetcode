class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        aloc = []
        bloc = []
        n = len(s)
        ma = len(a)
        mb = len(b)
        for i in range(n):
            if i <= n - ma and s[i:i+ma] == a:
                aloc.append(i)
            if i <= n - mb and s[i:i+mb] == b:
                bloc.append(i)
             
        ans = []
        # pt = 0
        for ai in aloc:
            # if ai in bloc:
            #     ans.append(ai)
            #     continue
            for bi in bloc:
                if abs(ai-bi) <= k:
                    ans.append(ai)
                    break
            
            
        return ans
        