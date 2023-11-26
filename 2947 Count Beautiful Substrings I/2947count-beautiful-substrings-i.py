class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_list = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        ans = 0
        for i in range(n):
            nvowels = 0
            ncons = 0
            for j in range(i,n):
                if s[j] in vowels_list:
                    nvowels += 1
                else:
                    ncons += 1
                if nvowels >= 1 and ncons == nvowels and (ncons * nvowels) % k == 0:
                    ans += 1
                    # print(s[i:j+1],i,j)
                
                

        
        return ans
        