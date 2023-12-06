class Solution:
    def totalMoney(self, n: int) -> int:
        div = n // 7
        rem = n % 7

        week0 = 28


        sm = 0
        for i in range(0,div):
            sm += week0 + i * 7

        rem += div
        sm += rem * (rem+1) // 2 - div * (div+1) // 2

        return sm
