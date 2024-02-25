class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        ans = 0
        n = len(bottomLeft)
        for i in range(n):
            xbi, xbj = bottomLeft[i]
            xti, xtj = topRight[i]
            for j in range(i+1,n):
                ybi, ybj = bottomLeft[j]
                yti, ytj = topRight[j]
                commoni = min(yti,xti)-max(xbi,ybi)
                commonj = min(ytj,xtj)-max(xbj,ybj)
                common = max(0,min(commoni,commonj))
                ans = max(ans,common **2)
                
                
                    
                    
        return ans