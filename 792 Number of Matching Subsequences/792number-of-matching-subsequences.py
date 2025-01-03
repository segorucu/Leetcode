class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        mp = collections.defaultdict(list)
        for i,a in enumerate(s):
            mp[a].append(i)

        count = 0
        for word in words:
            print(word)
            pt = 0
            for i,a in enumerate(word):
                ind = bisect.bisect_left(mp[a],pt)
                # print(ind)
                if ind == len(mp[a]):
                    break
                pt = mp[a][ind] + 1
            else:
                count += 1

        return count

        