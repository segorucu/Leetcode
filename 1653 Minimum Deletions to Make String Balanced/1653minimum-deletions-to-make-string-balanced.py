class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        n = len(s)
        Bsbefore = n * [0]
        Asafter = n * [0]

        for i in range(1,n):
            Bsbefore[i] = Bsbefore[i-1]
            if s[i-1] == 'b':
                Bsbefore[i] += 1
        for i in range(n-2,-1,-1):
            Asafter[i] = Asafter[i+1]
            if s[i+1] == 'a':
                Asafter[i] += 1

        # print(Bsbefore)

        ans = inf
        for a,b in zip(Bsbefore,Asafter):
            ans = min(ans,a+b)

        return ans
