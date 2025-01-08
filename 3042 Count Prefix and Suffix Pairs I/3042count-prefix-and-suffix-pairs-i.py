class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        n = len(words)
        count = 0
        for i in range(n-1):
            str1 = words[i]
            m1 = len(str1)
            for j in range(i+1,n):
                str2 = words[j]
                m2 = len(str2)
                if m2 < m1:
                    continue
                if str1[0:m1] == str2[0:m1] == str2[-m1:]:
                    count += 1

        return count
