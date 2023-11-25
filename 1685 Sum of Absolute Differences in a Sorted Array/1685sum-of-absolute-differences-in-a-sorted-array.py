class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        prefix = []
        sm = 0
        for num in nums:
            sm += num
            prefix.append(sm)
         
        n = len(nums)
        suffix = [prefix[-1]]
        for i in range(1,n):
            suffix.append(suffix[-1]-nums[i-1])
            
        
        ans = n*[0]
        for i in range(n):
            num = nums[i]
            ans[i] += suffix[i] + (2*i+1-n)*num - prefix[i]
            
        
        return ans