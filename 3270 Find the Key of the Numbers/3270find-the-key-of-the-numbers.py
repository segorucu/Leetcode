class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        ans = 0
        digit = 0
        while num1 > 0 and num2 > 0 and num3 > 0:
            curr = min(num1%10,num2%10,num3%10)
            ans += curr*(10**digit)
            num1 = num1 // 10
            num2 = num2 // 10
            num3 = num3 // 10
            digit += 1

        return ans