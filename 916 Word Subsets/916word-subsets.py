class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        

        counter = collections.defaultdict(int)
        for word in words2:
            c2 = collections.Counter(word)
            for key, val in c2.items():
                counter[key] = max(counter[key], val)

        # print(counter)
        ans = []
        for word in words1:
            c1 = collections.Counter(word)
            # print(word)
            for key in counter:
                # print(key, c2[key, c1[key]])
                if counter[key] > c1[key]:
                    break
            else:
                ans.append(word)

        return ans