class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        

        maxval = max(candidates)
        maxdigits = 1
        while maxval:
            maxval >>= 1
            maxdigits += 1

        counter = maxdigits * [0]
        n = len(candidates)

        for digit in range(maxdigits):
            for i in range(n):
                if candidates[i] & 1 == 1:
                    counter[digit] += 1
                candidates[i] = candidates[i] >> 1

    
        return max(counter)