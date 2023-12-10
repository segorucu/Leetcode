class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        n = len(nums)
        ans = set()

        def twoSum(start,target):
            left = start
            right = n - 1
            while right > left:
                if target + nums[left] + nums[right] > 0:
                    right -= 1
                elif target + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    ans.add((target,nums[left],nums[right]))
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            twoSum(i+1,num)


        return list(ans)

        


        

        

        