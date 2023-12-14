from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n = len(s)
        m = len(words)
        t = len(words[0])
        tm = t*m
        if tm >len(s):
            return []

        ans = []
        def check(counter,i):

            count = 0
            j = i
            while count < m:
                if s[j:j+t] in counter and counter[s[j:j+t]] > 0:
                    count += 1
                    counter[s[j:j+t]] -= 1
                    j += t
                else:
                    break
            else:
                ans.append(i)

        
        for i in range(n-tm+1):
            counter = Counter(words)
            check(counter,i)           


        return ans
        