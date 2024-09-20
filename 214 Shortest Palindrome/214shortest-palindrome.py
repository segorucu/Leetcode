class Solution:
    def getZarr(self, string, z):
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
        
    def search(self, text, pattern):
        concat = pattern + "$" + text
        start = len(pattern)
        l = len(concat)
        z = [0] * l
        self.getZarr(concat, z)
        count = 0
        for i in range(start,l):                
            if i+z[i] == l:
                break
        return concat[start+1:i]

    def shortestPalindrome(self, s: str) -> str:
        pattern = s
        text = s[::-1]
        res = self.search(text,pattern)
        return res+s

        