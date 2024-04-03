class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        exact = set(wordlist)

        lower = collections.defaultdict(str)
        for word in wordlist:
            if word.lower() not in lower:
                lower[word.lower()] = word

        asteriks = collections.defaultdict(str)
        for key in lower.keys():
            word = key.replace("a","*")
            word = word.replace("e","*")
            word = word.replace("i","*")
            word = word.replace("o","*")
            word = word.replace("u","*")
            if word not in asteriks:
                asteriks[word] = key

        # print(lower,asteriks)
        ans = []
        for q in queries:
            low = q.lower()
            ast = low.replace("a","*")
            ast = ast.replace("e","*")
            ast = ast.replace("i","*")
            ast = ast.replace("o","*")
            ast = ast.replace("u","*")
            if q in exact:
                ans.append(q)
            elif low in lower:
                ans.append(lower[low])
            elif ast in asteriks:
                ans.append(lower[asteriks[ast]])
            else:
                ans.append("")


        return ans

