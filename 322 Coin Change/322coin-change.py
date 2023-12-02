class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        L = (amount + 1) * [None]
        L[0] = 0
        for i in range(1,amount+1):
            L[i] = float('inf')
            for coin in coins:
                j = i - coin
                if j >= 0 and L[j] >= 0:
                    L[i] = min(L[i],L[j]+1)
            if L[i] == float('inf'):
                L[i] = -1

        return L[amount]