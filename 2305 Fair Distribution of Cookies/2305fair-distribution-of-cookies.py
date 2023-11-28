class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        ans = [100000000]
        n = len(cookies)
        def backtrack(sm,start,depth,zerocount):
            if depth == n:
                dum = max(sm)
                if dum < ans[0]:
                    ans[0] = dum
                    return
            for i in range(start,n):
                for child in range(k):
                    if n - depth == zerocount and sm[child] > 0:
                        continue
                    if sm[child] == 0:
                        substract = 1
                    else:
                        substract = 0
                    zerocount -= substract
                    sm[child] += cookies[i]
                    backtrack(sm,i+1,depth+1,zerocount)
                    zerocount += substract
                    sm[child] -= cookies[i]
 

        sm = k * [0]
        backtrack(sm,0,0,k)

        return ans[0]