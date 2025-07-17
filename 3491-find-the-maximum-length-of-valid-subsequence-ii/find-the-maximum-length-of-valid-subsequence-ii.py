class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        res = 2
        for x in range(k):
            mp = defaultdict(int)
            for num in nums:
                num = num % k
                mp[num] = mp[(x-num)%k] + 1
                res = max(res, mp[num])

        return res
                
        
