class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        count = 0
        n = len(nums)
        m = len(pattern)
        for i in range(n):
            for j in range(m):
                if i + j + 1 == n:
                    break
                if pattern[j] == 1:
                    if nums[i+j+1] <= nums[i+j]:
                        break
                elif pattern[j] == 0:
                    if nums[i+j+1] != nums[i+j]:
                        break
                elif pattern[j] == -1:
                    if nums[i+j+1] >= nums[i+j]:
                        break
            else:
                count += 1
                
                
        return count