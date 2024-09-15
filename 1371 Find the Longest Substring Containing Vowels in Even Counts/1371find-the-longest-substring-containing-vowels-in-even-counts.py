class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        vowelindex = {"a":0,"e":1,"i":2,"o":3,"u":4}
        prefixmp = collections.defaultdict(int)
        prefixmp[0] = -1
        bit = 0
        ans = 0
        for i,a in enumerate(s):
            if a in vowelindex:
                bit = bit ^ (1 << vowelindex[a])
            if bit in prefixmp:
                ans = max(ans,i-prefixmp[bit])
            else:
                prefixmp[bit] = i

        return ans
