class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        

        counter = {}
        n = len(candies)
        for i in range(k,n):
            c = candies[i]
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        maxval = len(counter)
        for i in range(k,n):
            c = candies[i]
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]

            prev = candies[i-k]
            if prev in counter:
                counter[prev] += 1
            else:
                counter[prev] = 1

            maxval = max(maxval, len(counter))


        return maxval