class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        def encrypt(x):
            digits = 0
            maxval = 0
            while x > 0:
                maxval = max(maxval,x%10)
                x = x // 10
                digits += 1
            x = 0
            for i in range(digits):
                x += maxval * (10**i)
            return x

        sm = 0
        for i,num in enumerate(nums):
            sm += encrypt(num)

        return sm