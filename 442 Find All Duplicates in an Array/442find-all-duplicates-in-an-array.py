class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        counter = collections.Counter(nums)
        ans = []
        for key, val in counter.items():
            if val == 2:
                ans.append(key)
        return ans