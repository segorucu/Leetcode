class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        counter = collections.Counter(s)
        odds = 0
        for key,val in counter.items():
            if val & 1 == 1:
                odds += 1

        return odds <= 1

        