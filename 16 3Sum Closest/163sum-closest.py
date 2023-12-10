class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = list(sorted(nums))
        n = len(nums)

        ans = float("inf")
        mindiff = float("inf")
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l < r:
                dum = num + nums[l] + nums[r]
                diff = abs(dum-target)
                if diff < mindiff:
                    mindiff = diff
                    ans = dum
                if dum > target:
                    r -= 1
                elif dum < target:
                    l += 1
                else:
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return ans
        
             

        