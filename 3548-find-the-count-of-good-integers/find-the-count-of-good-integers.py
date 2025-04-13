class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        if n == 1:
            count = 0
            for i in range(1,10):
                if i % k == 0:
                    count += 1
            return count
        

        fact = [factorial(i) for i in range(n+1)]
        def calc_combinations(counter):
            if "0" in counter:
                prod = (n-counter["0"]) * fact[n-1]
            else:
                prod = fact[n]
            for k,v in counter.items():
                    prod = prod // fact[v]
            return prod

        base = 10 ** ((n-1) // 2)
        end = base * 10
        skip = n & 1
        visited = set()
        count = 0
        for i in range(base,end):
            txt = str(i)
            txt += txt[::-1][skip:]
            if int(txt) % k == 0:
                sortedtxt = "".join(sorted(txt))
                visited.add(sortedtxt)
        # print(visited)
        count = 0
        for txt in visited:
            counter = Counter(txt)
            count += calc_combinations(counter)


        return count