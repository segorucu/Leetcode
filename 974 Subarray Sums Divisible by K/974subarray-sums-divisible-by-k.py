class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        counter = collections.Counter()
        counter[0] = 1

        ans = 0
        curr = 0
        for num in nums:
            curr += num
            curr %= k
            if curr in counter:
                ans += counter[curr]
            counter[curr] += 1
        return ans
