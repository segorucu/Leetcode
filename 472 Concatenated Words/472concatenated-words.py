from functools import cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        @cache
        def backtrack(curr, i, word):
            if i == len(word):
                return curr == 0 or curr in visited

            curr = curr * 26 + ord(word[i]) - base
            one = False
            if curr in visited:
                one = backtrack(0, i+1, word)
            two = backtrack(curr, i+1, word)
            return one or two

            
        words.sort(key = lambda x: len(x))
        visited = set()
        base = ord("a")-1
        ans = []
        for word in words:
            if backtrack(0,0,word):
                ans.append(word)
            curr = 0
            for letter in word:
                curr = curr * 26 + (ord(letter) - base)
            visited.add(curr)

        return ans