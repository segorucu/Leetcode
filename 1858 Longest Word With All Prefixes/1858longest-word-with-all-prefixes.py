class Hash:
    def __init__(self, s: str):
        self.hash_value = [0]
        self.p, self.m = 26, 10**9 + 7
        self.length = len(s)
        hash_so_far = 0
        p_pow = 1
        for i in range(self.length):
            hash_so_far = (hash_so_far + (1 + ord(s[i]) - ord('a')) * p_pow) % self.m
            self.hash_value.append(hash_so_far)
            p_pow = (p_pow * self.p) % self.m     

class Solution:
    
    def longestWord(self, words: List[str]) -> str:

        words.sort(key = lambda x: len(x))
        ans = ""
        seen = set()
        seen.add(0)
        for word in words:
            hs = Hash(word)
            seen.add(hs.hash_value[-1])
            for val in hs.hash_value:
                if val not in seen:
                    break
            else:
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word


        return ans
                