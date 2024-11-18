class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        

        n = len(code)
        ans = n * [0]
        if k == 0:
            return ans

        for i in range(n):
            curr = 0
            if k > 0:
                for j in range(1,k+1):
                    ind = i + j
                    curr += code[ind % n]
            elif k < 0:
                for j in range(k,0):
                    ind = i + j
                    curr += code[ind % n]
            ans[i] = curr
        return ans

