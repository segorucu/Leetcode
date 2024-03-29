class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seen = set()
        output = set()
        c = {'A' : 1, 'C' : 2, 'G' : 3, 'T' : 4}

        n = len(s)
        if n <= 10:
            return []

        curr = 0
        for i in range(10):
            curr += 4 ** (10-i-1) * c[s[i]]
            # print(i,curr)
        seen.add(curr)

        l = 0
        r = 10
        
        while r < n:
            curr = curr - c[s[l]] * (4 ** 9)
            curr *= 4
            curr += c[s[r]]
            r += 1
            l += 1
            if curr in seen:
                output.add(s[l:r])
            else:
                seen.add(curr)
            

        return output