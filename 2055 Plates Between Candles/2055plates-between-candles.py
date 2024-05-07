class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:


        candles = []
        for i, ch in enumerate(s):
            if ch == "|":
                candles.append(i)

        ans = []
        for left, right in queries:
            if left == right or not candles:
                ans.append(0)
                continue
            l = bisect_left(candles,left)
            l2 = candles[l]
            r = bisect_right(candles,right) - 1  
            r2 = candles[r]
            # print(l,r)
            if r2 <= l2:
                ans.append(0)
                continue
            plates = r2 - l2 - ( r - l) 
            ans.append(plates)
            
        # print(candles)


        return ans
        