class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort()
        n = len(tokens)
        if n == 0:
            return 0
        if power < min(tokens):
            return 0
        
        l = 0
        r = n - 1
        score = 0
        while l <= r:
            while l < n and l <= r and tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
            if l < r:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return score
