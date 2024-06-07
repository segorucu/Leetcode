class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        arr = sentence.split()
        lst = []
        for word in arr:
            curr = word
            for cand in dictionary:
                m = len(cand)
                if cand[:] == word[0:m]:
                    curr = min(cand,curr)
            lst.append(curr)


        return " ".join(lst)
        