class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ""
        val = num[0]
        count = 1
        for i in range(1,len(num)):
            if num[i] == val:
                count += 1
                if count == 3:
                    ans = max(ans,3*val)
            else:
                val = num[i]
                count = 1

        return ans