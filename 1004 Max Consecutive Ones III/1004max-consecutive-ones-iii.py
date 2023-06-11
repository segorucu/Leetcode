class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = dum = ans = curr = 0
        
        for right in range(len(nums)): 
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
                
            dum = right - left + 1
                
            ans = max(ans,dum)
        return ans
        