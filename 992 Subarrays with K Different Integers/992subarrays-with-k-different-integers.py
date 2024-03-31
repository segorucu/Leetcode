class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        

        counter = collections.defaultdict(int)
        l_far = l_near = 0
        n= len(nums)
        count = 0
        for r in range(n):
            counter[nums[r]] += 1
            while len(counter) > k:
                counter[nums[l_near]] -= 1
                if counter[nums[l_near]] == 0:
                    counter.pop(nums[l_near])
                l_near += 1
                l_far = l_near

            while counter[nums[l_near]] > 1:
                counter[nums[l_near]] -= 1
                l_near += 1

            if len(counter) == k:
                count += (l_near - l_far + 1)
        return count

        