class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:


        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        if len(sentence1) >= len(sentence2):
            large = sentence1
            small = sentence2
        else:
            large = sentence2
            small = sentence1

        n = len(large)
        m = len(small)
        small = collections.deque(small)
        l = 0
        r = n-1
        while small:
            if small[0] == large[l]:
                small.popleft()
                l += 1
            elif small[-1] == large[r]:
                small.pop()
                r -= 1
            else:
                return False

        return True

        
        