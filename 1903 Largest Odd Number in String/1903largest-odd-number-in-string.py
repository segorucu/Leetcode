class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = {"1","3","5","7","9"}

        ans = ""
        n = len(num)
        for i in range(n-1,-1,-1):
            if num[i] in odd:
                ans = num[0:i+1]
                break

        return ans
            
        