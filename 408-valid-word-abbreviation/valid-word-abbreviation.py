class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        n = len(word)

        wi = 0
        i = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == "0":
                    return False
                curr = []
                while i < len(abbr) and abbr[i].isdigit():
                    curr.append(abbr[i])
                    i += 1
                curr = "".join(curr)
                wi += int(curr)
            else:
                if wi >= n or abbr[i] != word[wi]:
                    return False
                wi += 1
                i += 1

        return wi == n