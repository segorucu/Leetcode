from functools import cache
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        nums.sort()
        
        counter = collections.defaultdict(int)
        def backtrack(i,kept):
            if i == len(nums):
                if kept > 0:
                    return 1
                else:
                    return 0

            tot = 0
            if counter[nums[i]-k] == 0:
                counter[nums[i]] += 1
                tot += backtrack(i+1,kept+1)
                counter[nums[i]] -= 1
            tot += backtrack(i+1,kept)
            return tot
            

        return backtrack(0,0)

        