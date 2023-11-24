class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)
        def backtrack(j,curr):
            
            if len(curr) > n:
                return
            
            curr = sorted(curr)
            if curr[:] not in ans:
                ans.append(curr[:])
            for i in range(j,n):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
            
        
        backtrack(0,[])
        ans = sorted(ans)
        return ans