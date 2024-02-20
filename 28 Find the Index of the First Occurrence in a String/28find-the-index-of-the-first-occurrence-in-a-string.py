class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        m = len(needle)
        n = len(haystack)
        def getZarr(string, z):
            n = len(string)
            l, r, k = 0, 0, 0
            for i in range(1, n):
                if i > r:
                    l, r = i, i
                    while r < n and string[r - l] == string[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
                else:
                    k = i - l
                    if z[k] < r - i + 1:
                        z[i] = z[k]
                    else:
                        l = i
                        while r < n and string[r - l] == string[r]:
                            r += 1
                        z[i] = r - l
                        r -= 1
                
        def search(text, pattern):
            concat = pattern + "$" + text
            start = len(pattern)
            l = len(concat)
            z = [0] * l
            getZarr(concat, z)
            # print(z)
            count = 0
            for i in range(start,l):                
                if z[i] == start:
                    return i-start-1
            return -1
        
        return search(haystack, needle)
        