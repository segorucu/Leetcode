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
        m = len(pattern)
        start = m+1
        l = len(concat)
        z = [0] * l
        self.getZarr(concat, z)
        count = 0
        arr = []
        for i in range(start,l):
            if z[i] == m:
                arr.append([i-start,i-start+m])
        return arr

    def addBoldTag(self, s: str, words: List[str]) -> str:

        if len(words) == 0:
            return s

        indices = []
        for word in words:
            indices += self.search(s,word)
        indices.sort()
        if len(indices) == 0:
            return s

        combined = [indices[0]]
        for i in range(1,len(indices)):
            if indices[i][0] <= combined[-1][1]:
                combined[-1][1] = max(combined[-1][1],indices[i][1])
            else:
                combined.append(indices[i])

        ans = ""
        prev = 0
        for st,e in combined:
            ans += s[prev:st]
            ans += "<b>" + s[st:e] + "</b>" 
            prev = e
        if e != len(s):
            ans += s[e:]


        return ans
        