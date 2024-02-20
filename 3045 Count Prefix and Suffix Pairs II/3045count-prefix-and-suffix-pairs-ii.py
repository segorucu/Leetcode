class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        MOD = 10**20+9
        
        # storing frequency of previous word hashes
        hmap = collections.defaultdict(int)
        ord0 = ord('a')-1
        res = 0

        for word in words:

            candidates = set()
            prefix = 0
            mult = 1
            for l in word:
                prefix = (prefix * 26 + (ord(l)-ord0)) % MOD
                if prefix in hmap:
                    candidates.add(prefix)
            suffix = 0
            mult = 1
            for l in word[::-1]:
                suffix = (suffix + mult * (ord(l)-ord0)) % MOD
                if suffix in candidates:
                    res += hmap[suffix]
                mult = (mult*26) % MOD
            hmap[prefix] += 1

        
        return res