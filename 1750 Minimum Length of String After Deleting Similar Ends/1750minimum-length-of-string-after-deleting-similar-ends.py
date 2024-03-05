class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)
        if n == 1:
            return 1
        keys = []
        group = []
        for k,g in itertools.groupby(s):
            keys.append(k)
            group.append(len(list(g)))
        if keys == list(reversed(keys)):
            if len(keys) % 2 == 0:
                return 0
            else:
                k = group[len(keys) // 2]
                if k == 1:
                    return 1
                else:
                    return 0

        m = len(keys)
        l = 0
        r = m-1
        while l < r and keys[l] == keys[r]:
            n -= group[l]
            n -= group[r]
            l += 1
            r -= 1
        return n
        