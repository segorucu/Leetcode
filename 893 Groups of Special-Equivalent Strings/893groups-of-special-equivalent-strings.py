class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        seen = set()
        for word in words:
            even = []
            odd = []
            for i, char in enumerate(word):
                if i % 2 == 0:
                    even.append(char)
                else:
                    odd.append(char)
            key = ("".join(sorted(even)), "".join(sorted(odd)))
            seen.add(key)

        return len(seen)
                