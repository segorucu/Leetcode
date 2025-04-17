class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        count = 0
        for i, ni in enumerate(nums):
            for j in range(i+1,n):
                if (i * j) % k == 0 and ni == nums[j]:
                    count += 1

        return count