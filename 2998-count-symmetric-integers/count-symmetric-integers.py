class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0
        for i in range(low, high+1):
            txt = str(i)
            if len(txt) % 2:
                continue
            
            mid = len(txt) // 2
            left = 0
            for j in range(mid):
                left += int(txt[j])
            right = 0
            for j in range(mid,len(txt)):
                right += int(txt[j])
            if left == right:
                count += 1

        return count