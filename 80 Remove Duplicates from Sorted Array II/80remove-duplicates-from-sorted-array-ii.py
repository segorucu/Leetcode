from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        n = len(nums)

        p1 = p2 = 0  
        while p1 < len(nums):
            val = nums[p1]
            counter[val] += 1
            if counter[val] > 2:
                nums.pop(p1)
                continue
            p1 += 1
            # if counter[val] <= 2:
            #     p2 += 1
            # if p1 != p2:
            #     if p1 < n:
            #         nums[p2] = nums[p1]


        return len(nums)

        
