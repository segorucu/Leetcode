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
            
    def search(self, text, pattern):
        concat = pattern + "$" + text
        start = len(pattern)
        l = len(concat)
        z = [0] * l
        self.getZarr(concat, z)
        return z[len(pattern)+1:]

    def minValidStrings(self, words, target):
        # Generate all prefixes for the given words
        graph = collections.defaultdict(int)
        for word in words:
            res = self.search(target,word)
            for i in range(len(target)):
                graph[i] = max(graph[i], res[i])
        
        n = len(target)
        dp = (n+1) *[inf]
        dp[0] = 0
        for i in range(n):
            for j in range(1,graph[i]+1):
                dp[i+j] = min(dp[i+j],dp[i]+1)
        
        if dp[-1] == inf:
            return -1

        return dp[-1]  # If no valid sequence found
