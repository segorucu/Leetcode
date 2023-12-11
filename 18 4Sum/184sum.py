class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        ans = []
        for i, num0 in enumerate(nums):
            if i > 0 and num0 == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                num1 = nums[j]
                l = j+1
                r = n-1
                while l < r:
                    dum = num0 + num1 + nums[l] + nums[r]
                    if  dum > target:
                        r -= 1
                        while nums[r] == nums[r+1] and l < r:
                            r -= 1
                    elif dum < target:
                        l += 1
                    else:
                        ans.append([num0, num1, nums[l],nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
    
        return ans
        