from collections import Counter
from heapq import heapify, heappush, heappop
class Words:
    def __init__(self,word):
        self.word = word
    def __lt__(self,other):
        return self.word > other.word

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        lst = []
        for char in s:
            heappush(lst,Words(char))
            
        ans = ""
        repeat = 0
        repeated = ""
        stash = []
        while lst:
            char = heappop(lst).word
            if char in repeated:
                if repeat >= repeatLimit:
                    stash.append(char)
                    continue
                else:
                    repeat += 1
                    ans += char
            else:
                repeated = char
                repeat = 1
                ans += char
                if stash:
                    repeat = 0
                    while stash:
                        ans += stash.pop()
                        repeat += 1
                        repeated = ans[-1]
                        if repeat == repeatLimit:
                            break
        while stash and repeat < repeatLimit:
            ans += stash.pop()
            repeat += 1
        return ans