class Solution:
    def triangleType(self, nums: List[int]) -> str:
        for i in range(3):
            sm = 0
            for j in range(3):
                if i != j:
                    sm += nums[j]
            if sm <= nums[i]:
                return "none"
            
        unique = set(nums)
        if len(unique) == 3:
            return "scalene"
        elif len(unique) == 2:
            return "isosceles"
        else:
            return "equilateral"
        