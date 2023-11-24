class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        def backtrack(j,curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for i in range(j,n+1):   
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()

        backtrack(1,[])
        return ans
        