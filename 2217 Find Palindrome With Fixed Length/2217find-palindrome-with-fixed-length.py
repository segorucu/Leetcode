class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        
        N = (intLength + 1) // 2
        prev = pow(10,N-1)-1
        maxval = pow(10,N) - 1
        for i, query in enumerate(queries):
            val = prev + query
            valstr = str(val)
            if val > maxval:
                queries[i] = -1
            else:
                if intLength % 2 == 1:
                    valstr = valstr + valstr[-2::-1]
                else:
                    valstr = valstr + valstr[::-1]
                queries[i] = int(valstr)



        return queries