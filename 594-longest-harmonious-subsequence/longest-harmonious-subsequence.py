class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        ans = 0
        counter = Counter(nums)

        for k,v in counter.items():
            if k-1 in counter:
                ans = max(ans, v + counter[k-1])

        return ans