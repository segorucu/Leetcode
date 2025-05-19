class Solution:
    def triangleType(self, nums: List[int]) -> str:
        counter = Counter(nums)
        n = len(counter.keys())
        maxval = max(nums)
        sm = sum(nums)
        if maxval >= sm / 2:
            return "none"
            
        if n == 3:
            return "scalene"
        elif n == 2:
            return "isosceles"
        else:
            return "equilateral"
        