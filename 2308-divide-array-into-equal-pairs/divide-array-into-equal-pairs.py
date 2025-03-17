class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        counter = collections.Counter(nums)
        for k,v in counter.items():
            if v%2==1:
                return False
        return True