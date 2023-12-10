class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
        n = len(variables)
        ans = []
        for i in range(n):
            [ai, bi, ci, mi] = variables[i]
            val = 1
            for j in range(bi):
                val = (val * ai) % 10
            
            valn = 1
            for j in range(ci):
                valn = (valn * val) % mi
                
            if valn == target:
                ans.append(i)
                
        return ans