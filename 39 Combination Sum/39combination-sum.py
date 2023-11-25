class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        ans = []
        def backtrack(j,sm,curr):
            if sm == target:
                ans.append(curr[:])
                return
            elif sm > target:
                return

            for i in range(j,n):
                curr.append(candidates[i])
                backtrack(i,sm+candidates[i], curr)
                curr.pop()

        backtrack(0,0,[])
        return ans