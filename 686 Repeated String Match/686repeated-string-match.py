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
        # print("hello2")
        # print(z)
        for i in range(start,l):                
            if z[i] == start:
                return True
        return False

    def repeatedStringMatch(self, a: str, b: str) -> int:
        m = len(a)
        n = len(b)
        count = n // m
        text = count * a
        # print("hello")
        if self.search(text,b):
            return count
        count += 1
        text = text + a
        if self.search(text,b):
            return count
        count += 1
        text = text + a
        if self.search(text,b):
            return count
        return -1
        