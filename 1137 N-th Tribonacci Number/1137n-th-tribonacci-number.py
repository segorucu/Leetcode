class Solution:
    def tribonacci(self, n: int) -> int:
        
        m = max(3,n)
        T = [0 for _ in range(m+1)]
        T[1] = 1
        T[2] = 1

        for i in range(3,n+1):
            T[i] = T[i-1] + T[i-2] + T[i-3]

        return T[n]