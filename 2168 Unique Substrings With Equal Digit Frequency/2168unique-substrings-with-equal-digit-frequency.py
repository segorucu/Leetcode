class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        
        
        visited = set()

        n = len(s)
        for i in range(n):
            counter = collections.defaultdict(int)
            for j in range(i,n):
                counter[s[j]] += 1
                prev = None
                for key,val in counter.items():
                    if not prev:
                        prev = val
                    else:
                        if prev != val:
                            break
                else:
                    visited.add(s[i:j+1])


        return len(visited)