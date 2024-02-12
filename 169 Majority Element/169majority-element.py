class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        maxkey = None
        maxvel = -float("inf")
        for key,val in counter.items():
            if val > maxvel:
                maxkey = key
                maxvel = val

        return maxkey
        