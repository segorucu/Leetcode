class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        mn = {}
        ans = -float("inf")
        curr = 0
        for num in nums:
            if num in mn:
                mn[num] = min(mn[num],curr)
            else:
                mn[num] = curr

            curr += num

            for y in [num-k,num+k]:
                if y in mn:
                    ans = max(ans,curr-mn[y])
            
           
        if ans == -float("inf"):
            return 0 
        return ans