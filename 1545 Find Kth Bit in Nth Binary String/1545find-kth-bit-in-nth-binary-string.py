class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        k -= 1
        def go(k,n):
            if n == 1:
                return 0

            tot_size = pow(2,n)-1
            first_half = tot_size // 2
            if k == first_half:
                return 1
            elif k < first_half:
                return go(k, n-1)
            else:
                k = k - (first_half+1)
                k = first_half-1 - k
                return go(k,n-1) ^ 1


        return str(go(k,n))