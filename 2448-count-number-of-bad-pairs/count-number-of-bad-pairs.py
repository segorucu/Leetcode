class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = n * (n-1) // 2
        mp = collections.defaultdict(int)
        goods = 0
        for i,num in enumerate(nums):
            goods += mp[num-i]
            mp[num-i] += 1



        return total - goods