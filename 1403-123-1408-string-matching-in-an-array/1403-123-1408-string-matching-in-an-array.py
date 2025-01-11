class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words.sort(key=lambda x: len(x), reverse=True)
        library = set()
        ans = []
        for word in words:
            if word in library:
                ans.append(word)
            n = len(word)
            for i in range(n):
                for j in range(i,n):
                    print(word[i:j+1])
                    library.add(word[i:j+1])

        return ans

