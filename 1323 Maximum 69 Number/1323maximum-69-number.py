class Solution:
    def maximum69Number (self, num: int) -> int:

        num = str(num)
        for i,s in enumerate(num):
            if s == "6":
                num = num[0:i] + "9" + num[i+1:]
                break
            
        return int(num)
