class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        seen = set()
        ans = []
        for num in nums:
            if num in seen:
                ans.append(num)
            else:
                seen.add(num)


        return ans