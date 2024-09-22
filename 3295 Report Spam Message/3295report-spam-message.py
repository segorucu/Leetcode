class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        
        bannedWords = set(bannedWords)
        count = 0
        for word in message:
            if word in bannedWords:
                count += 1

        return count >= 2