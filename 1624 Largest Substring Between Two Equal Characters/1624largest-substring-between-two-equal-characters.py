from collections import defaultdict
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        counter = defaultdict(list)
        for i,a in enumerate(s):
            counter[a].append(i)
            
        ans = -1
        for key,vals in counter.items():
                ans = max(ans,max(vals) - min(vals) - 1)

        return ans

        


        return 0