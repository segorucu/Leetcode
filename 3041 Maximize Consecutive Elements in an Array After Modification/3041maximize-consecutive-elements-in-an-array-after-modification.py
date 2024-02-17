from functools import cache
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        
        nums.sort()
        counter = collections.Counter(nums)
        n = len(nums)

        @cache
        def backtrack(curr,used):

            ans = 0
            if counter[curr] > 0:
                counter[curr] -= 1
                ans += backtrack(curr+1,True)+1
                counter[curr] += 1
            ans2 = 0
            if counter[curr-1] > 0:
                counter[curr-1] -= 1
                ans2 += backtrack(curr+1,False)+1
                counter[curr-1] += 1
            return max(ans,ans2)


        ans = 1
        for key in counter.keys():
            ans = max(ans,backtrack(key,False))
            ans = max(ans,backtrack(key+1,False))
        
        return ans
                
        