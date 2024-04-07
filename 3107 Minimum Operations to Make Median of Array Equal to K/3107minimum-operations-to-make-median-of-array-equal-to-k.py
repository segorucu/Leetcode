class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            return abs(nums[0]-k)
        
        nums.sort()
        if len(nums) % 2 >= 0:
            med = len(nums) // 2
            if k == nums[med]:
                return 0
            elif k > nums[med]:
                pt = med
                ans = 0
                while pt < len(nums) and nums[pt] < k:
                    ans += (k-nums[pt])
                    pt += 1
                return ans
            elif k < nums[med]:
                pt = med
                ans = 0
                while pt >= 0 and nums[pt] > k:
                    ans += (nums[pt]-k)
                    pt -= 1
                return ans
#         else:
#             med1 = len(nums) // 2 -1
#             if nums[med1] <= k <= nums[med1+1]:
#                 curr = nums[med1+1]-k
                
#                 diff = 2*abs(k-curr)
#                 return int(diff)
#             elif k < nums[med1]:
#                 pt = med1
#                 ans = 0
#                 while pt > 0 and nums[pt] > k:
#                     ans += (nums[pt]-k)
#                     pt +- 1
#                 return ans
#             elif k > nums[med1+1]:
#                 pt = med1+1
#                 ans = 0
#                 while pt < len(nums) and nums[pt] < k:
#                     ans += (k-nums[pt])
                # return ans
                

            
        