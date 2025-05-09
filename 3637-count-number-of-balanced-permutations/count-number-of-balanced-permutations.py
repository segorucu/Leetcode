class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        

        counter = Counter()
        sm = 0
        for n in num:
            n = int(n)
            counter[n] += 1
            sm += n

        if sm % 2:
            return 0

        balance = sm // 2
        even_count = len(num) // 2
        odd_count = len(num) - even_count
        MOD = 10**9 + 7

        @cache
        def dfs(digit, even_count, odd_count, balance):
            if even_count == 0 and odd_count == 0 and balance == 0:
                return 1
            if digit < 0 or even_count < 0 or odd_count < 0 or balance < 0:
                return 0

            sm = 0
            for j in range(counter[digit]+1):
                odd = j
                even = counter[digit] - j
                if odd_count - odd < 0 or even_count - even < 0:
                    continue
                odd_comb = comb(odd_count,odd)
                even_comb = comb(even_count,even)

                sm += odd_comb * even_comb * dfs(digit-1,even_count-even,odd_count-odd,balance-odd*digit)
            return sm % MOD

        return dfs(9,even_count, odd_count, balance)