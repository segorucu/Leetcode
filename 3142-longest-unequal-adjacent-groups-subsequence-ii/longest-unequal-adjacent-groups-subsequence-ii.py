class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(groups)
        dp = n * [1]
        pathmp = defaultdict(list)

        def valid(i, j):
            str1 = words[i]
            str2 = words[j]
            if len(str1) != len(str2):
                return False
            if groups[i] == groups[j]:
                return False

            diff = 0
            for lt1, lt2 in zip(str1, str2):
                if lt1 != lt2:
                    diff += 1

            return diff == 1

        ans = []
        for i in range(n):
            pathmp[i] = [words[i]]
            for j in range(i):
                if valid(i,j) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    pathmp[i] = pathmp[j] + [words[i]]
            if len(pathmp[i]) > len(ans):
                ans = pathmp[i]

        return ans

