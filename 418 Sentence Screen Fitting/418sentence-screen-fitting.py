class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        for word in sentence:
            if len(word) > cols:
                return 0
        
        sentence = " ".join(sentence) + " "
        n = len(sentence)
        total_len = 0
        for r in range(rows):
            total_len += cols
            if sentence[total_len%n] == " ":
                pass
            else:
                while sentence[total_len%n] != " ":
                    total_len -= 1
            total_len += 1

        return total_len // n