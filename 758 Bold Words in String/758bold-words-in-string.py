from heapq import heapify, heappush, heappop
class Solution:
    def getZarr(self, string, z):
# z returns the number of letter matches starting from the beginning.
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
            
    def search(self, text, pattern, arr):
        concat = pattern + "$" + text
        start = len(pattern)
        l = len(concat)
        z = [0] * l
        self.getZarr(concat, z)
        count = 0
        for i in range(start,l):                
            if z[i] == start:
                beg = i-start-1
                end = beg + start
                heappush(arr,(beg,end))
        return
    def boldWords(self, words: List[str], s: str) -> str:

        arr = []
        for word in words:
            self.search(s,word,arr)

        if not arr:
            return s

        brackets = []
        beg, end = heappop(arr)
        brackets.append([beg,end])
        while arr:
            beg, end = heappop(arr)
            if beg > brackets[-1][1]:
                brackets.append([beg,end])
            else:
                brackets[-1][1] = max(end,brackets[-1][1])

        ans = ""
        prevend = 0
        for beg, end in brackets:
            ans += s[prevend:beg]
            ans += "<b>" + s[beg:end] + "</b>"
            prevend = end
        ans += s[end:]

        return ans
        