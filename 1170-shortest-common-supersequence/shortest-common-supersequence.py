class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        n1 = len(str1)
        n2 = len(str2)
        dp = [(n2+1)*[0] for _ in range(n1+1)]

        for i in range(n1):
            for j in range(n2):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

        locations = []
        i = n1
        j = n2
        while dp[i][j] > 0:
            if str1[i-1] == str2[j-1]:
                locations.append((i-1,j-1))
                i -= 1
                j -= 1
            else:
                if dp[i][j] == dp[i][j-1]:
                    j -= 1
                else:
                    i -= 1

        locations.reverse()
        
        if not locations:
            return str1 + str2

        
        p1 = p2 = 0
        ans = []
        iloc = 0
        while p1 < n1 and p2 < n2 and iloc < len(locations):
            while p1 < locations[iloc][0]:
                ans.append(str1[p1])
                p1 += 1
            while p2 < locations[iloc][1]:
                ans.append(str2[p2])
                p2 += 1
            ans.append(str1[p1])
            p1 += 1
            p2 += 1
            iloc += 1
        while p1 < n1:
            ans.append(str1[p1])
            p1 += 1
        while p2 < n2:
            ans.append(str2[p2])
            p2 += 1

        return "".join(ans)
        