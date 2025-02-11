class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        counter = Counter(nums)
        ans = []
        for k,v in counter.items():
            if v > n // 3:
                ans.append(k)
        return ans