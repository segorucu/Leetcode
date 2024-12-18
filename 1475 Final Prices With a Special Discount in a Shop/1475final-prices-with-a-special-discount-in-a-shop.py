class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        ans = []
        n = len(prices)
        for i in range(n):
            found = False
            for j in range(i+1,n):
                if prices[j] <= prices[i]:
                    found = True
                    break
            if found:
                ans.append(prices[i]-prices[j])
            else:
                ans.append(prices[i])

        return ans
