class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        # def = checkvalid()
        
        n = len(s)
        ans = 2
        for i in range(n):
            counter = collections.defaultdict(int)
            for j in range(i,n):
                counter[s[j]] += 1
                if counter[s[j]] >= 3:
                    ans = max(ans,j-i)
                    break
            else:
                ans = max(ans,j-i+1)
        return ans
                
                
            