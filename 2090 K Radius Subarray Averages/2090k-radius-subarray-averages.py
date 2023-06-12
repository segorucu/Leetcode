class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix = [nums[0]]
        n = len(nums)
        
        for i in range(1,n):
            prefix.append(prefix[i-1]+nums[i])
            
        average = []
        for i in range(n):
            if (i-k) < 0 or (i+k) >= n:
                average.append(-1)
                continue
            average.append((prefix[i+k]-prefix[i-k]+nums[i-k]) // (2*k+1))
            
        return average
                