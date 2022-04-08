class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        test = strs[0]
        if len(strs) == 1: return test
        for i,c in enumerate(test):
            for st in strs:
                try:
                    if c != st[i]:
                        return test[0:i]
                except:
                    return max("",test[0:i])
        return test
                
            
        