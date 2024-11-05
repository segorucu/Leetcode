class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        gcd0 = numsDivide[0]
        m = len(numsDivide)
        for i in range(1,m):
            gcd0 = math.gcd(gcd0, numsDivide[i])

        nums.sort()
        n = len(nums)
        for i in range(n):
            if gcd0 % nums[i] == 0:
                return i
            if nums[i] > gcd0:
                break
        return -1