class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = collections.defaultdict(int)
        ans = []
        for st in strs:
            dum = "".join(sorted(st))
            if dum in mp:
                ans[mp[dum]].append(st)
            else:
                ans.append([st])
                mp[dum] = len(ans)-1

        return ans
        