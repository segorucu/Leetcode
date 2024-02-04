from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        found = False
        left = right = 0
        n = len(s)
        m = len(t)
        counter = Counter(t)
        visited = defaultdict(int)
        def canmove(left):
            c = s[left]
            if c not in counter:
                return True
            if c in counter:
                if visited[c] > counter[c]:
                    visited[c] -= 1
                    return True
                else:
                    return False


        while right < n:
            c = s[right]
            if c not in counter.keys():
                pass
            elif c in counter.keys() and not found:   
                visited[c] += 1
                for key,val in counter.items():
                    if val > visited[key]:
                        break
                else:
                    found = True
                    while canmove(left):
                        left += 1
                    ans = s[left:right+1]

            elif c in counter.keys() and found:
                visited[c] += 1
                while canmove(left):
                    left += 1
                if len(ans) > right - left + 1:
                    ans = s[left:right+1]
                    
            right += 1
                    
                
        if not found:
            return ""

        return ans


        