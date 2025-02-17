class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        

        counter = Counter(tiles)
        n = len(tiles)
        def backtrack(i):
            if i == n:
                return 0

            tot = 0
            for k,v in counter.items():
                if v == 0:
                    continue
                counter[k] -= 1
                tot += backtrack(i+1) + 1
                counter[k] += 1

            return tot

        return backtrack(0)


                