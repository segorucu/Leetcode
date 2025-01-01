class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        data = []
        for ind, source, target in zip(indices,sources,targets):
            data.append([ind,source,target])
        data.sort()

        mp = collections.defaultdict(tuple)
        for ind, source, target in data:
            curr = s[ind:ind+len(source)]
            if curr == source:
                mp[ind] = (len(source),target)


        prev = 0
        arr = []
        for ind,val in mp.items():
            w, target = val
            if prev < ind:
                arr.append(s[prev:ind])
                prev = ind
            arr.append(target)
            prev = ind + w
        n = len(s)
        if prev < n:
            arr.append(s[prev:n])

        return "".join(arr)