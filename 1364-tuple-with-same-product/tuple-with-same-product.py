class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        mp = collections.defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                mp[nums[i]*nums[j]] += 1

        ans = 0
        for k,v in mp.items():
            if v == 1:
                continue
            totpairs = 2*v
            ans += totpairs * (totpairs - 2)

        return ans