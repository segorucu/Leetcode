from bisect import bisect_left
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        prefix = []
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)

        n = len(nums)
        ans = []
        for q in queries:
            ind = bisect_left(nums,q)
            if ind == n or ind == 0:
                cost = abs(n * q - prefix[-1])
                ans.append(cost)
            else:
                cost = ind * q - prefix[ind-1]
                cost += prefix[-1] - prefix[ind-1] - (n-ind) * q
                ans.append(cost)

        return ans