class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        counter = Counter(s)
        alphabet = string.ascii_lowercase
        MOD = 10**9 + 7
        for _ in range(t):
            prev = counter["a"]
            for l, r in pairwise(alphabet):
                nxt = counter[r]
                counter[r] = prev
                prev = nxt
            counter["a"] = prev
            counter["b"] += (prev % MOD)
            counter["b"] = counter["b"] % MOD

        return sum(counter.values()) % MOD
                