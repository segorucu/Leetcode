class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        counter = Counter(answers)
        ans = 0

        for k,v in counter.items():
            upto = k + 1
            while v > 0:
                ans += upto
                v -= upto

        return ans


