from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        rev = collections.defaultdict(list)
        for key,val in counter.items():
            rev[val].append(key)

        ans = ""
        sortedkeys = sorted(rev.keys(),reverse=True)
        for key in sortedkeys:
            for val in rev[key]:
                ans += key * val

        return ans