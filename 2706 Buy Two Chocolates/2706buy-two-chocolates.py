class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices.sort()
        val = money - prices[0] - prices[1]
        if  val >= 0:
            return val
        else:
            return money