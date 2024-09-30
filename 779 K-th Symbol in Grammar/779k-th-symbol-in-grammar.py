class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        if k <= 2:
            return k-1

        val = self.kthGrammar(n-1, math.ceil(k / 2))
        if val == 1:
            return k % 2
        else:
            return (k+1) % 2




        return selfkthGrammar(n, k)