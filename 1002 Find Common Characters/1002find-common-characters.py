class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        counter = collections.Counter(words[0])

        n = len(words)
        for i in range(1,n):
            word = words[i]
            for key,val in counter.items():
                cnt = word.count(key)
                counter[key] = min(counter[key],cnt)

        ans = []
        for key, val in counter.items():
            for i in range(val):
                ans.append(key)



        return ans